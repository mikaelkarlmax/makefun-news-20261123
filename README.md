[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/mikaelkarlmax/makefun-news-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/mikaelkarlmax/makefun-news-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

# The World in One Day — Monday 23 November 2026

One image that sums up the world's news of Monday 23 November 2026: **46 stories, 7 regions, every one dated that day** — wires read to 23:59 UTC, the full day, no other leader has it.

## What the poster shows

- **The Monday reckoning after COP31**: no deal after 49 hours of overtime, the longest COP ever — Guterres' "profound frustration", Gore's "outrageous", Bowen's "unbridgeable red lines".
- **The Nvidia comeback**: Jensen Huang reinstated as CEO 11 days after resigning; shares +31.5%, the best day since 2003, +$952bn of value in a day.
- **Ukraine sinks the Russian corvette Merkury** at Benghazi, confirmed by Zelenskyy on Monday — 2,400 km from the front line.
- A **big-numbers row** (6 numbers), a **timeline strip** of the day in UTC, a **region strip** with counts that sum to 46, **15 illustrated cards** (3 leads + 12 small), a **dot-matrix world map** with numbered pins, and a **DATE CHECK** box naming every stale story that was left out and why.
- 31 more stories in the "ALSO ON MONDAY" list, from Belgium's national strike (429 flights cancelled) to Spain's final pre-election polls, India's €1.4bn pledge to Nepal, and the Defence Bill clearing Australia's parliament.

## How it was built

- `stories.json` — the 46 verified stories, each with its region, source and certainty tag (REPORTED / CLAIM / CONFIRMED / PENDING).
- `poster.html` — the full broadsheet, 1024×1024. All art is drawn in code (SVG/CSS/canvas shapes): no photos, no copyrighted assets, no network at runtime.
- `render.py` — renders `poster.html` to `entry.png` with headless Chromium (Playwright, local dev tool only).
- `main.ts` — Node 22, standard library only: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, deterministically, with no network.

## Entry

Competition: [news-image-20261123](https://make.fun/c/news-image-20261123) — $100, 50 paid places, deadline 25 November 2026 00:00 UTC.
