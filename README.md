# Portfolio — Joris van den Ende

Static site, no build step. Plain HTML and one stylesheet, ready for GitHub Pages.

## Pages

| Route | File | Status |
| --- | --- | --- |
| `/` | `index.html` | Ready |
| `/work/cbr/` | `work/cbr/index.html` | Ready |
| `/work/statiegeld/` | `work/statiegeld/index.html` | Ready |
| `/work/mijnpensioenoverzicht/` | `work/mijnpensioenoverzicht/index.html` | Ready |
| `/work/flyr-labs/` | `work/flyr-labs/index.html` | Ready |
| `/about/` | `about/index.html` | Short pitch and contact |
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

## Structure

```
assets/css/site.css     All styles. Colour tokens at the top; mobile first, wider layouts from 760 px and 900/1024 px.
assets/fonts/           Inter Tight (variable, latin + latin-ext), self-hosted. Licence: OFL-LICENSE.txt
assets/img/             Project screens as WebP, derived from the original portfolio material.
assets/video/           CBR prototype recording (MP4, no sound) and its poster image.
assets/js/video.js      Play button for the video: no autoplay; native controls without JavaScript.
```

Phone frames are pure CSS (`.phone`): a thin dark border and a soft shadow around a complete screen. Change a frame's size with the `--w` custom property.

## Images and video

All screens are WebP files in `assets/img/`, made from the original project material
with `tools/build_images.py` (not needed to run the site).

- Every screen in a phone frame has the same ratio (9:19.5). Screens that were slightly
  wider or narrower are brought to that ratio by extending flat background only
  (tab-bar area, dark backdrop edges). Nothing is stretched or cut off.
- Long or partial screens (the Mijnpensioenoverzicht "before" pages and the amounts
  detail) are shown flat, outside a phone frame (`.flat`).
- The two CBR question screens from the earlier export had text running outside its
  answer boxes, so they are no longer used.
- `assets/video/cbr-prototype.mp4` is the CBR prototype recording (v5), 51 s, no audio
  track. The poster is its first frame.

## Open points

- LinkedIn: no link is shown until the URL is known.
- Mijnpensioenoverzicht: the year of the project (only shown once known).
- Mijnpensioenoverzicht screens are 390 px wide; a 2× export from Figma would look sharper.
