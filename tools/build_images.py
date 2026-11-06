"""Build the site's WebP screens from the original project images.

- Phone screens: near-white borders trimmed from every side, so nothing
  light shows between the screen and the phone frame.
- Statiegeld success modals: the light corners outside the rounded sheet
  are filled with the sheet's own colours.
- Desktop (FLYR) screens: resized only.
"""
import glob
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

SRC = Path(sys.argv[1])          # folder with src/ (sg, mpo, flyr/img)
OLD = Path(sys.argv[2])          # portfolio deck asset folder
OUT = Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)


def find(folder, prefix):
    return Image.open(glob.glob(str(folder / f"{prefix}*"))[0]).convert("RGB")


def trim_light(im, max_px=60, fixed_top=0):
    """Trim light borders. With fixed_top, the top is cut by exactly that many
    pixels instead (CBR: keeps a little air above the chapter header)."""
    a = np.asarray(im).astype(int)

    def light(line):
        return line.mean() > 232 and line.std() < 10

    h, w, _ = a.shape
    t = 0
    while not fixed_top and t < max_px and light(a[t]):
        t += 1
    if fixed_top:
        t = fixed_top
    b = 0
    while b < max_px and light(a[h - 1 - b]):
        b += 1
    l = 0
    while l < max_px and light(a[:, l]):
        l += 1
    r = 0
    while r < max_px and light(a[:, w - 1 - r]):
        r += 1
    return im.crop((l, t, w - r, h - b)), (t, b, l, r)


def fix_modal_corners(im):
    w, h = im.size
    top = (0, 0, 0)
    bottom = im.getpixel((w // 2, h - 4))
    for (x, y, col) in [(0, 0, top), (w - 1, 0, top), (0, h - 1, bottom), (w - 1, h - 1, bottom)]:
        ImageDraw.floodfill(im, (x, y), col, thresh=40)
    return im


def save(im, name, width=None):
    if width and im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(OUT / f"{name}.webp", "WEBP", quality=86, method=6)
    print(f"{name:28s} {im.size[0]}x{im.size[1]}")


phone = {
    # CBR prototype (780 wide); the empty status-bar strip at the top is removed
    "cbr-reflect-examday": (find(OLD, "093e8ec2"), 24),
    "cbr-reflect-moment": (find(OLD, "1bb3da6b"), 24),
    "cbr-check": (find(OLD, "c7bb3ffc"), 24),
    "cbr-plan": (find(OLD, "6b268af0"), 0),
    # Statiegeld app screens, already trimmed to the screen edge
    "statiegeld-home": (find(SRC / "sg", "home"), 0),
    "statiegeld-check": (find(SRC / "sg", "check"), 0),
    "statiegeld-scan": (find(SRC / "sg", "scan"), 0),
    "statiegeld-map": (find(SRC / "sg", "map"), 0),
    "statiegeld-wf-scanner": (find(SRC / "sg", "wfscanner"), 0),
    "statiegeld-wf-credited": (find(SRC / "sg", "wfcredited"), 0),
    "statiegeld-wf-stash": (find(SRC / "sg", "wfstash"), 0),
    # Mijnpensioenoverzicht
    "mpo-before-intro": (find(SRC / "mpo", "before1"), 0),
    "mpo-before-amounts": (find(SRC / "mpo", "before2"), 0),
    "mpo-overview": (find(SRC / "mpo", "overview"), 0),
    "mpo-age-open": (find(SRC / "mpo", "dd"), 0),
    "mpo-estimate": (find(SRC / "mpo", "popup"), 0),
    "mpo-breakdown": (find(SRC / "mpo", "bedragen"), 0),
}
for name, (im, top) in phone.items():
    out, cut = trim_light(im, fixed_top=top)
    if any(cut):
        print(f"  trimmed {name}: top {cut[0]}, bottom {cut[1]}, left {cut[2]}, right {cut[3]}")
    save(out, name, 600)

# Side panels: the white panel reaching the edge is the design itself, so no trim
save(find(SRC / "mpo", "aow"), "mpo-aow", 600)
save(find(SRC / "mpo", "provider"), "mpo-providers", 600)

for name, key in [("statiegeld-success-cola", "m1"), ("statiegeld-success-fuze", "m2"), ("statiegeld-success-tonic", "m3")]:
    save(fix_modal_corners(find(SRC / "sg", key)), name)

flyr = SRC / "flyr" / "img"
for name, key, w in [
    ("flyr-before", "4d7fbe", 1400),
    ("flyr-filter-strip", "456346", 1135),
    ("flyr-drawer-original", "d464d1", 426),
    ("flyr-drawer-explored", "f3af47", 720),
    ("flyr-separate", "a0b26b", 1392),
    ("flyr-final", "c0aae4", 1438),
    ("flyr-expanded", "f69597", 742),
    ("flyr-collapsed", "6cc268", 1392),
    ("flyr-groups", "83cac7", 760),
]:
    save(find(flyr, key), name, w)
save(find(OLD, "d216db79"), "flyr-add-section", 728)
