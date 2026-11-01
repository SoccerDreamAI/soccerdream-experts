#!/usr/bin/env python3
"""Generate the GitHub social preview card (1280x640).

GitHub has no API for uploading a social preview, so this file is generated
locally and uploaded by hand at Settings -> General -> Social preview.

Only ASCII is drawn. A missing glyph in a social card is a tofu box on every
share of the repository, which is exactly the kind of detail that makes a
project look abandoned.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
OUT = os.path.join("docs", "assets", "social-preview.png")

# Same palette as the README hero: near-black terminal, cyan accent, amber warn.
BG_TOP = (11, 18, 32)
BG_BOTTOM = (6, 10, 20)
GRID = (20, 32, 54)
FG = (226, 232, 240)
DIM = (122, 138, 160)
CYAN = (56, 189, 248)
AMBER = (251, 191, 36)
RED = (248, 113, 113)

FONT_DIR = os.environ.get("WINDIR", r"C:\Windows") + r"\Fonts"


def font(name, size):
    for cand in (os.path.join(FONT_DIR, name), name):
        try:
            return ImageFont.truetype(cand, size)
        except OSError:
            continue
    return ImageFont.load_default()


f_mono = font("consola.ttf", 26)
f_mono_sm = font("consola.ttf", 21)
f_mono_xs = font("consola.ttf", 18)
f_bold = font("arialbd.ttf", 52)
f_body = font("arial.ttf", 27)


def main():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)

    # vertical gradient
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)

    # faint grid
    for x in range(0, W, 40):
        d.line([(x, 0), (x, H)], fill=GRID)
    for y in range(0, H, 40):
        d.line([(0, y), (W, y)], fill=GRID)

    # amber accent bar, echoes the product's title bar
    d.rectangle([0, 0, W, 6], fill=AMBER)

    x0 = 78
    d.text((x0, 54), "SoccerDream Expert Team", font=f_mono_sm, fill=CYAN)

    d.text((x0, 104), "Disagreement is escalated,", font=f_bold, fill=FG)
    d.text((x0, 168), "never averaged.", font=f_bold, fill=AMBER)

    d.text((x0, 258), "Four specialists. A claim gets challenged, defended,", font=f_body, fill=DIM)
    d.text((x0, 294), "or withdrawn on evidence. Output is a range and a", font=f_body, fill=DIM)
    d.text((x0, 330), "confidence level, not a number chosen to look certain.", font=f_body, fill=DIM)

    # miniature transcript, so the card shows the mechanism rather than claiming it
    y = 400
    lines = [
        ("stage 2/4  specialists", "4 reads, 2 disagree", CYAN),
        ("stage 3/4  challenge", "B challenges A: too narrow", AMBER),
        ("stage 4/4  review", "1 claim withdrawn", RED),
        ("conclusion", "range, confidence medium", FG),
    ]
    for label, val, col in lines:
        d.text((x0, y), label, font=f_mono_xs, fill=DIM)
        d.text((x0 + 300, y), val, font=f_mono_xs, fill=col)
        y += 30

    d.line([(x0, 540), (x0 + 470, 540)], fill=GRID)
    d.text((x0, 558), "source-available, not open source", font=f_mono_sm, fill=DIM)
    d.text((x0 + 470, 558), "·", font=f_mono_sm, fill=GRID)
    d.text((x0 + 500, 558), "github.com/SoccerDreamAI", font=f_mono_sm, fill=CYAN)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes", img.size)


if __name__ == "__main__":
    main()
