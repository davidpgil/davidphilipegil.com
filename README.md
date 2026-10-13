# davidphilipegil.com

Portfolio website of David Philipe Gil, Creative Technologist.

Live site: https://davidphilipegil.com

## Structure

- Root: the built static site — HTML pages, `style.css`, `app.js`, `favicon.svg`, `img/`, `fonts/`, and the resume PDF
- `build/`: the generator script `build_v2.py`, with its helper `_meta.py` and project data `projects.json`

## Build

```
python build/build_v2.py
```

This regenerates the HTML pages, sitemap, robots.txt and favicon in the repo root and adds a fresh `?v=` version stamp to the CSS and JS links.

## Hosting

It is a plain static site with no server-side code.

## Fonts

Inter and Space Grotesk are licensed under the SIL Open Font License 1.1. The license texts are in `fonts/`.

The resume PDF, `David_Philipe_Gil_Resume.pdf`, is included at the repository root.
