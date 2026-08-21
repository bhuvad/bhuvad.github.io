#!/usr/bin/env python3
"""Refresh Bioconductor download counts in the site HTML.

Bioconductor publishes a per-package stats table at

    <base>/packages/stats/<category>/<pkg>/<pkg>_stats.tab

with one row per month plus a yearly "all" row.  We sum the monthly
``Nb_of_downloads`` column, i.e. TOTAL downloads, not distinct IPs.

The script rewrites elements tagged with ``data-pkg`` in the HTML, plus the
site-wide totals.  If a package cannot be fetched its existing value is left
untouched and a warning is printed -- an outage upstream must not block a
deploy or blank out the numbers.

Usage:
    update_download_stats.py [--base-url URL] [--check] FILES...
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from datetime import date, timezone, datetime

DEFAULT_BASE = "https://bioconductor.org"

# Bioconductor splits packages across repositories; try each in turn rather
# than hard-coding a guess per package.
CATEGORIES = ("bioc", "data-experiment", "workflows", "data-annotation")

TIMEOUT = 30


def fetch_total_downloads(pkg: str, base_url: str) -> tuple[int, str] | None:
    """Return (total downloads, category) for a package, or None if unavailable."""
    for category in CATEGORIES:
        url = f"{base_url}/packages/stats/{category}/{pkg}/{pkg}_stats.tab"
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT) as resp:
                if resp.status != 200:
                    continue
                text = resp.read().decode("utf-8", "replace")
        except Exception:
            continue

        total = parse_total(text)
        if total is not None:
            return total, category
    return None


def parse_total(text: str) -> int | None:
    """Sum the monthly Nb_of_downloads rows of a Bioconductor stats table."""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return None

    header = re.split(r"\t+|\s{2,}|\s+", lines[0].strip())
    try:
        i_dl = header.index("Nb_of_downloads")
        i_month = header.index("Month")
    except ValueError:
        return None

    total = 0
    seen = False
    for ln in lines[1:]:
        parts = re.split(r"\t+|\s{2,}|\s+", ln.strip())
        if len(parts) <= max(i_dl, i_month):
            continue
        month = parts[i_month]
        if month.lower() == "all":       # yearly subtotal -- skip, we sum months
            continue
        try:
            total += int(parts[i_dl])
        except ValueError:
            continue
        seen = True
    return total if seen else None


def human_short(n: int) -> str:
    """1234567 -> '1.2M'; 242297 -> '242k'."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1_000:
        return f"{n // 1000}k"
    return str(n)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--check", action="store_true",
                    help="report what would change without writing")
    args = ap.parse_args()

    sources = {p: open(p, encoding="utf-8").read() for p in args.files}

    # every package referenced anywhere in the given files
    pkgs = sorted({m for src in sources.values()
                   for m in re.findall(r'data-pkg="([^"]+)"', src)})
    if not pkgs:
        print("no data-pkg elements found -- nothing to do", file=sys.stderr)
        return 1

    counts: dict[str, int] = {}
    failed: list[str] = []
    for pkg in pkgs:
        got = fetch_total_downloads(pkg, args.base_url)
        if got is None:
            failed.append(pkg)
            print(f"  WARN  {pkg:<24} unavailable - keeping existing value")
            continue
        counts[pkg], category = got
        print(f"  ok    {pkg:<24} {counts[pkg]:>12,}  ({category})")

    if not counts:
        print("ERROR: no package stats could be retrieved; leaving files unchanged",
              file=sys.stderr)
        return 0 if not args.check else 1

    total_all = sum(counts.values())
    # packages we could not reach still contribute their committed value
    for pkg in failed:
        for src in sources.values():
            m = re.search(r'data-pkg="' + re.escape(pkg) + r'"[^>]*>([\d,]+)<', src)
            if m:
                total_all += int(m.group(1).replace(",", ""))
                break

    asof = datetime.now(timezone.utc).strftime("%B %Y")
    print(f"\n  total {total_all:,} downloads across {len(pkgs)} packages (as of {asof})")

    changed = False
    for path, src in sources.items():
        out = src
        for pkg, n in counts.items():
            out = re.sub(r'(data-pkg="' + re.escape(pkg) + r'"[^>]*>)[^<]*(<)',
                         lambda m, n=n: f"{m.group(1)}{n:,}{m.group(2)}", out)
        out = re.sub(r'(class="[^"]*\bdl-total\b[^"]*"[^>]*>)[^<]*(<)',
                     lambda m: f"{m.group(1)}{total_all:,}{m.group(2)}", out)
        out = re.sub(r'(class="[^"]*\bdl-total-short\b[^"]*"[^>]*>)[^<]*(<)',
                     lambda m: f"{m.group(1)}{human_short(total_all)}{m.group(2)}", out)
        out = re.sub(r'(class="[^"]*\bdl-asof\b[^"]*"[^>]*>)[^<]*(<)',
                     lambda m: f"{m.group(1)}{asof}{m.group(2)}", out)
        if out != src:
            changed = True
            if args.check:
                print(f"  would update {path}")
            else:
                open(path, "w", encoding="utf-8").write(out)
                print(f"  updated {path}")

    if not changed:
        print("  (no changes needed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
