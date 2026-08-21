# bhuvad.github.io

Personal academic website of [Dharmesh D Bhuva](https://bhuvad.github.io/) — computational systems
biologist and NHMRC Emerging Leadership Fellow at the Frazer Institute, University of Queensland.

## About this site

The site is plain, dependency-free HTML and CSS — no static site generator, no build step.

```
index.html          # About: bio, interests, appointments, education, awards
publications.html   # All refereed publications and preprints
software.html       # R/Bioconductor packages and web apps
talks.html          # Conference talks, seminars, and workshops
css/style.css       # All styling (light/dark via prefers-color-scheme)
img/                # Images
```

## Download counts

The Bioconductor download numbers on the software and home pages are not
hand-maintained. Elements tagged `data-pkg="<package>"` (plus the `dl-total`,
`dl-total-short`, and `dl-asof` classes) are rewritten at publish time by
`scripts/update_download_stats.py`, which sums the **total downloads** column
of each package's [Bioconductor stats table](https://bioconductor.org/packages/stats/)
— not distinct IPs.

The deploy workflow runs it on every push to `main` and once a week on a
schedule. If Bioconductor is unreachable the script warns and leaves the
committed values in place, so an upstream outage never fails a deploy or
blanks out the numbers. The values checked into git are therefore a fallback,
superseded on the next successful deploy.

To refresh the committed values locally:

```sh
python3 scripts/update_download_stats.py software.html index.html
```

Add `--check` to see what would change without writing.

## Editing

Edit the HTML files directly and push to `main`. The GitHub Actions workflow
(`.github/workflows/gh-pages.yml`) publishes the repository to the `gh-pages` branch, which GitHub
Pages serves at <https://bhuvad.github.io/>.

To preview locally, open the files in a browser or run any static server, e.g.:

```sh
python3 -m http.server
```

## Licence

Content © Dharmesh D Bhuva. Code released under the [MIT Licence](LICENSE.md).
