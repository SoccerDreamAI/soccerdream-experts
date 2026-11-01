"""Render the README hero GIF: a team run where one claim is forced to withdraw.

Pure PIL + ffmpeg. No network, no fonts to install beyond Windows defaults.

    python scripts/make-hero-gif.py

Writes frames to .gif-build/ and calls ffmpeg to assemble docs/assets/team-run.gif.
"""
import os
import shutil
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 820, 420
PAD_X = 28
TOP = 62
LINE_H = 25

BG = (13, 17, 23)
BAR = (22, 27, 34)
FG = (201, 209, 217)
DIM = (110, 118, 129)
GREEN = (63, 185, 80)
RED = (248, 81, 73)
YELLOW = (210, 153, 34)
BLUE = (88, 166, 255)
CYAN = (86, 212, 221)

FONT_PATHS = [
    "C:/Windows/Fonts/consola.ttf",
    "C:/Windows/Fonts/cour.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
]


def load_font(size):
    for p in FONT_PATHS:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


MONO = load_font(15)
MONO_B = load_font(15)
TINY = load_font(12)

# (text, colour) — each entry is one rendered line
# NOTE: ASCII only. consola.ttf has no glyph for U+2713, which renders as a tofu box.
SCRIPT = [
    ("$ sd team run teams/example-team.yaml --event demo-001", FG),
    ("", FG),
    ("stage 1/4  context      +  2 sources normalized", GREEN),
    ("stage 2/4  specialists  +  4 reads, 2 disagree", GREEN),
    ("stage 3/4  challenge    >  B challenges A: \"too narrow\"", YELLOW),
    ("              A cites 2 figures, B cites 1", DIM),
    ("              -> B withdraws", RED),
    ("stage 3/4  challenge    +  1 claim withdrawn", GREEN),
    ("stage 4/4  review       +  high -> medium", GREEN),
    ("", FG),
    ("conclusion  range 1.2 - 2.4, confidence: medium", CYAN),
    ("            no single outcome named (by design)", DIM),
    ("", FG),
    ("exit 0", DIM),
]


def frame(n_lines, cursor=True, blink=True):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # title bar
    d.rectangle([0, 0, W, 34], fill=BAR)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([14 + i * 19, 12, 24 + i * 19, 22], fill=c)
    d.text((W // 2 - 34, 9), "sd — team run", font=TINY, fill=DIM)
    d.line([0, 34, W, 34], fill=(48, 54, 61))

    y = TOP
    for i, (text, colour) in enumerate(SCRIPT[:n_lines]):
        if text:
            d.text((PAD_X, y), text, font=MONO, fill=colour)
        y += LINE_H

    if cursor and blink:
        cy = TOP + (n_lines - 1) * LINE_H
        last = SCRIPT[n_lines - 1][0] if n_lines <= len(SCRIPT) else ""
        cw = d.textlength(last, font=MONO) if last else 0
        d.rectangle([PAD_X + cw + 2, cy + 3, PAD_X + cw + 10, cy + 17], fill=FG)

    return img


def main():
    out_dir = os.path.join("docs", "assets")
    build = ".gif-build"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(build, exist_ok=True)
    for f in os.listdir(build):
        os.remove(os.path.join(build, f))

    idx = 0
    # reveal lines one at a time
    for i in range(1, len(SCRIPT) + 1):
        for blink in (True, False):
            img = frame(i, cursor=(i < len(SCRIPT)), blink=blink)
            img.save(os.path.join(build, f"f{idx:03d}.png"))
            idx += 1

    # hold the finished frame long enough to read
    final = frame(len(SCRIPT), cursor=False)
    for _ in range(6):
        final.save(os.path.join(build, f"f{idx:03d}.png"))
        idx += 1

    gif_path = os.path.join(out_dir, "team-run.gif")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-framerate", "4",
        "-i", os.path.join(build, "f%03d.png"),
        "-vf", "split[s0][s1];[s0]palettegen=max_colors=64[p];[s1][p]paletteuse=dither=bayer",
        "-loop", "0",
        gif_path,
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)
    shutil.rmtree(build, ignore_errors=True)

    size = os.path.getsize(gif_path)
    print(f"wrote {gif_path}  ({size/1024:.0f} KB, {idx} frames)")
    if size > 3 * 1024 * 1024:
        print("WARNING: over 3 MB — reduce frames or colours", file=sys.stderr)


if __name__ == "__main__":
    main()
