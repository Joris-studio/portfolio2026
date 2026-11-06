# Portfolio — Joris van den Ende

Static site, no build step. Plain HTML and one stylesheet, ready for GitHub Pages.

## Pages

| Route | File | Status |
| --- | --- | --- |
| `/` | `index.html` | Review version |
| `/work/cbr/` | `work/cbr/index.html` | Review version |
| `/work/statiegeld/` | `work/statiegeld/index.html` | Review version |
| `/work/mijnpensioenoverzicht/` | `work/mijnpensioenoverzicht/index.html` | Review version |
| `/work/flyr-labs/` | `work/flyr-labs/index.html` | Review version |
| `/about/` | `about/index.html` | Placeholder, still to be written |
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

All screens are WebP files in `assets/img/`, made from the original project material.
Phone screens are trimmed so no white or light border shows between the screen and the
phone frame; the Statiegeld success messages have their light corners filled with the
sheet's own colours. The script that does this is `tools/build_images.py` (not needed to
run the site).

- `cbr-*`: CBR prototype screens.
- `statiegeld-*`: Statiegeld app screens, success messages and wireframes.
- `mpo-*`: Mijnpensioenoverzicht, existing site (`before`) and prototype screens. These
  are 390 px wide; a 2× export from Figma would look sharper.
- `flyr-*`: FLYR desktop screens (shown without phone frame).

## Open points

- Home intro is draft copy.
- CBR: exact role, team and period; whether the flow was tested and went live; the reasoning behind the plan that grows while you answer.
- Statiegeld: role, team and process contribution; status wording (‘concept design’ or ‘concept and early build’).
- Mijnpensioenoverzicht: verify the gross and net constraint.
- FLYR Labs: job title, exact role in the filters project, permission to show FLYR material.
- LinkedIn URL (no LinkedIn link is shown until it is known).
- About page.
