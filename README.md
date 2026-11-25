# Sum up 24 November's world news in one image

Entry for https://make.fun/bounty/news-image-20261124

- Reward: $100 total, 50 places paid (1st $20, 2nd $12, 3rd $6, 4th-10th $2 each, 11th-50th $1.20 each)
- Deadline: Thu 2026-11-26 00:00 UTC (08:00 CST)
- Free to enter, no entry fee

## What it does

`main.py` (Python 3.13, standard library only, no network) copies
the bundled `asset.png` to `/output/entry.png`.

The image is a 1024x1024 PNG, 78,552 bytes, with five labelled stories
from Tuesday 24 November 2026:

1. Riyadh tower hit again — Houthi drone, 2nd strike in under a week, 11 injured
2. Nvidia falls 6% — after Jensen Huang's return rally
3. Hormuz tankers hit — Iran's Revolutionary Guard says mines hit tankers
4. Zaporizhzhia struck — Russian strike kills 2, wounds 40+ in Ukraine
5. Shenzhou-24 to launch — China to launch with Pakistan's first astronaut aboard

Sources checked 2026-11-25: Reuters / SRN News, RTHK, and the 24 Nov
world-news briefing. The Shenzhou item is worded "to launch" because
the launch itself was scheduled for the morning of 25 Nov.

## Run it

```sh
python3 main.py
# Wrote /output/entry.png (78552 bytes, sha256 5f1e318e5b018469264f77d80e7a4d721dde34e721c2de7862d3a7dbd4c612ed)
```

Verified locally: two runs write identical bytes (same sha256 above),
1024x1024, under the 1 MiB limit, no network.

## Files

- `main.py` — the entry program
- `asset.png` — the image it copies
- `build_image.py` — how `asset.png` was drawn (Pillow, local build only; not needed at run time)
- `LICENSE` — MIT

## Notes / risks

- This entry was built in a Muse chat session, not in a recorded
  coding-agent session with provider token usage. make.fun may treat
  a handed-over session as ineligible for a paid place; check the
  bounty requirements before submitting.
- Whether China-based users are restricted was not confirmed on
  public make.fun pages.
- Nothing here has been submitted or claimed. Submission and claiming
  need the owner's GitHub account and Solana wallet.
