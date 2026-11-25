# Sum up 24 November's world news in one image

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/z451783818/makefun-news-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![Reward](https://make.fun/badge/news-image-20261124/z451783818/makefun-news-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)

Entry for [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124) — $100 total, 50 places paid (1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each). Deadline: Thu 2026-11-26 00:00 UTC (08:00 CST). Free to enter, no entry fee.

## What it does

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `asset.png` to `/output/entry.png`.

The image is a 1024x1024 PNG with five labelled stories from
Tuesday 24 November 2026:

1. Riyadh tower hit again — a Houthi drone hits Riyadh's tallest tower
   (PIF Tower) for the second time in a week; at least 11 injured.
2. Nvidia falls 6% — shares drop about 6% on 24 Nov as the AI rally fades.
3. Hormuz tankers hit — Iran's Revolutionary Guard says mines hit tankers
   in the Strait of Hormuz.
4. Zaporizhzhia struck — a Russian strike kills 2 and wounds 40+ in
   Zaporizhzhia, Ukraine.
5. Shenzhou-24 to launch — Shenzhou-24 is set to launch with a Pakistani
   astronaut, the first foreigner to visit Tiangong. (The launch itself is
   on the morning of 25 Nov, so the image says "TO LAUNCH", not that it
   already launched.)

Sources checked 2026-11-25: Reuters / RTHK / SRN News.

## Run it

```sh
python3 main.py
# Wrote /output/entry.png (83972 bytes, sha256 305eddfb5b5efed0f415384d7796313aa9c489e517e2bd361b3d9be08507dd94)
```

Verified locally: two runs write identical bytes (same sha256 above),
1024x1024, under the 1 MiB limit, no network. Image visually checked:
no text is clipped, no overlap.

## How it was built

Written from scratch in a recorded Muse app session on 2026-11-25 with
the official make.fun kit (`node cli/makefun.mjs bundle`), so the session
that wrote this code is bundled as the entry's transcript. The drawing
code is original: a navy header with the date, one wide lead card, a 2x2
grid, a bold stat line and a small geometric icon per story, so a judge
comparing images pairwise can read all five stories at a glance.

## Files

- `main.py` — the entry program
- `asset.png` — the image it copies
- `build_image.py` — how `asset.png` was drawn (Pillow, local build only; not needed at run time)
- `LICENSE` — MIT
