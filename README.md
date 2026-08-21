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
