# davidphilipegil.com

Portfolio website of David Philipe Gil, Creative Technologist.

Live site: https://davidphilipegil.com

## Structure

- `src/projects.json`: the single source of project data, including titles, categories, tools, image sizes and alt text
- `src/content.json`: home page capabilities, the tools marquee and resume content
- `src/templates/`: page templates using Python `string.Template` placeholders
- `src/static/`: hand-written assets copied as-is, including `style.css`, `app.js`, `favicon.svg`, `img/`, `fonts/` and the resume PDF
- `src/build.py`: the build script, standard library only
- `dist/`: generated output, not committed

## Build

```
python3 src/build.py
```

This wipes `dist/`, copies `src/static/` into it, renders every page, sitemap and robots.txt, and stamps the CSS and JS links with a fresh `?v=` version so browsers pick up changes. Nothing in `src/` is written by the build.

To preview locally:

```
cd dist && python3 -m http.server 8000
```

Deploy by uploading the contents of `dist/`. It is a plain static site with no server-side code.

## Fonts

Inter and Space Grotesk are licensed under the SIL Open Font License 1.1. The license texts are in `src/static/fonts/`.
