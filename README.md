# Portfolio — Joris van den Ende

Static site, no build step. Plain HTML and one stylesheet, ready for GitHub Pages.

## Pages

| Route | File | Status |
| --- | --- | --- |
| `/` | `index.html` | Designed (review version) |
| `/work/cbr/` | `work/cbr/index.html` | Designed (review version) |
| `/work/statiegeld/` | `work/statiegeld/index.html` | Placeholder, case still to be written |
| `/work/mijnpensioenoverzicht/` | `work/mijnpensioenoverzicht/index.html` | Placeholder |
| `/work/flyr-labs/` | `work/flyr-labs/index.html` | Placeholder |
| `/about/` | `about/index.html` | Placeholder |
| — | `404.html` | Not-found page |

All internal links are relative, so the site works both as a user site (`username.github.io`), on a custom domain, and as a project site (`username.github.io/repo/`). The only exception is the homepage link in `404.html`, which points to `/`; on a project site, change it to `/repo/`.

## Publishing on GitHub Pages

1. Put the contents of this folder in the root of a repository (keep `.nojekyll`).
2. In the repository: Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. For a custom domain, add a `CNAME` file containing the domain, for example `joris.studio`.

Preview locally with a small server (folder links such as `work/cbr/` need one):

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

## Review mode

This is a review version:

- Every page has `class="review"` on `<html>`. That shows the dashed coral tags marking draft copy and facts still to confirm. Remove the class to hide all tags at once.
- Every page has `<meta name="robots" content="noindex">`. Remove it when the site may be found by search engines.

## Structure

```
assets/css/site.css     All styles. Colour tokens at the top; mobile first, wider layouts from 760 px and 900/1024 px.
assets/fonts/           Inter Tight (variable, latin + latin-ext), self-hosted. Licence: OFL-LICENSE.txt
assets/img/             Project screens as WebP, derived from the original portfolio material.
```

Phone frames are pure CSS (`.phone`): a thin dark border and a soft shadow around a complete screen. Change a frame's size with the `--w` custom property.

## Images

| File | Source | Size |
| --- | --- | --- |
| `cbr-reflect-moment.webp` | CBR prototype, reflection question (multiple choice) | 600 × 1298 |
| `cbr-reflect-examday.webp` | CBR prototype, ‘Hoe begon je examendag?’ | 600 × 1298 |
| `cbr-check.webp` | CBR prototype, ‘Dit zien we tot nu toe’ | 600 × 1298 |
| `cbr-plan.webp` | CBR prototype, ‘Dit is jouw plan.’ | 600 × 1298 |
| `statiegeld-check.webp` | Statie Check | 520 × 1086 |
| `statiegeld-stash.webp` | Statie Stash home | 520 × 1095 |
| `statiegeld-map.webp` | Statie Map | 520 × 1088 |
| `mpo-before.webp` | Mijnpensioenoverzicht, current site (before) | 520 × 1177 |
| `mpo-after.webp` | Mijnpensioenoverzicht, redesign (after) | 390 × 844 — low resolution, replace with a 2× export |
| `flyr-add-section.webp` | FLYR, in-table ‘Add section’ proposal | 728 × 390 |

## Open points

- Home intro is draft copy.
- CBR: exact role, team and period; whether the flow was tested and went live; the reasoning behind the plan that grows while you answer.
- LinkedIn URL (no LinkedIn link is shown until it is known).
- Statiegeld, Mijnpensioenoverzicht and FLYR Labs case pages, and the About page, are still to be written.
- Statiegeld screens still show the iOS status bar from the original screenshots.
