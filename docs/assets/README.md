# Assets

## Required

| File | Size | Used by |
|:--|:--|:--|
| `team-run.gif` | 820px wide, < 3 MB | `README.md`, `README.zh-CN.md` hero |
| `social-preview.png` | 1280 × 640 | Repository social preview (set in GitHub settings, not linked from the repo) |

## Rules for `team-run.gif`

The hero GIF is the highest-leverage asset in this repository. It decides, in about three
seconds, whether a visitor reads the rest.

**Must:**

- Show a **disagreement being resolved**. Two members conflict, one yields with a cited
  reason. That interaction *is* the product — a diagram of boxes will not carry it.
- Reach comprehension within ~3 seconds, no title card, no logo intro.
- Loop cleanly. No visible jump at the boundary.
- Use neutral placeholder data. No real fixtures, no real odds, no currency symbols.

**Must not:**

- Contain betting terminology, stake amounts, or a "recommended pick" panel.
- Show a leaderboard, a hit-rate chart, or anything resembling a performance claim.
- Be a screen recording with a cursor wandering around. Crop and speed it up.

## Producing it

Any of these work; the second is fastest if you already have the CLI:

```bash
# 1. from a scripted terminal session
asciinema rec demo.cast && agg demo.cast team-run.gif

# 2. from a screen recording, cropped and sped up
ffmpeg -i raw.mov -vf "crop=1280:720:0:0,setpts=0.6*PTS,fps=12,scale=820:-1" \
       -loop 0 team-run.gif
```

Check the result at 820px wide in both GitHub light and dark themes before committing —
a GIF that only reads on a light background looks broken to half your audience.
