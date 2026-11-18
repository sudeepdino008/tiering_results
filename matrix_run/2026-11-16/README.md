# Matrix run: lookback × SSD merge limit (stage 17)

Updated 2026-11-18T01:01:10Z. 15/26 cells done, running 1mo/4.

Each cell: 10,000 chaintip blocks 25,400,001..25,410,000 from W = 25,400,000, demotion on, offline BALs, state cache on,
`--tiering.cold-io-max-mbps=50`, erigon c604cf14, 64 GiB memory scope (page cache included), page caches dropped before the start.
L = lookback (cold boundary = W − L), M = SSD merge limit for commitment files (`--tiering.commitment-hot-merge-steps`).
Cold files are pre-merged and on HDD; hot files on SSD are merged up to M steps. All-SSD baseline (256-step merges):
277 Mgas/s per block, SSD commitment ≈ 300 GB (`baseline_allssd_merged_6mo_w25400000_2026-10-23-3`).
Mgas/s per block = mean of the per-block value; SSD/HDD GB = commitment `.kv` bytes per tier at the run end.

### W2 (second start block, for 9mo)

W2 = 26,130,000. Cells marked `@W2` (diamonds in the frontier) run blocks 26,130,001..26,140,000 from base `tv2_1s_base_w2`.
Commitment data below block 24,091,854 is one 180 GB file (0-8192), and tiering moves only whole files. At W the 9mo boundary
is 25,400,000 − 1,944,000 = 23,456,000, inside that file, so nothing could go to HDD. At W2 it is 24,186,000, above it.
`6mo@W2/32` is the anchor: compared with `6mo/32` at W, it shows how much the block range alone changes the numbers.
12mo would need W2 ≥ ~26.69M, beyond the data on this box (ends at 26,147,580).


## Charts

![frontier](frontier.png)

![trends](trends.png)

![progress](progress.png)

## Cells (in run order, `order.txt`)

| # | L | M | Mgas/s per block | wall Mgas/s | commit p50 / p95 / p99 ms | SSD GB | HDD GB | hot files | SSD / HDD probes per block | demotions (GB) | cold merges | duration h | rc / root err / OOM / peak GiB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [6mo/32](cells/6mo_m32/) | 32 | 138.1 | 62.5 | 85.6 / 693.7 / 1,457.1 | 265.0 | 185.6 | 33 | 7,752 / 286 | 0 (0) | 0 | 1.35 | 0 / 0 / 0 / 64.0 |
| 2 | [3mo/64](cells/3mo_m64/) | 64 | 79.3 | 38.9 | 177.8 / 1,946.9 / 4,350.6 | 100.1 | 247.6 | 9 | 4,624 / 543 | 0 (0) | 0 | 2.16 | 0 / 0 / 0 / 64.0 |
| 3 | [6mo/1](cells/6mo_m1/) | 1 | 69.2 | 37.8 | 155.6 / 1,731.0 / 3,799.0 | 729.4 | 189.3 | 1,043 | 162,433 / 278 | 5 (6.0) | 3 | 2.23 | 0 / 0 / 0 / 64.0 |
| 4 | [6mo/128](cells/6mo_m128/) | 128 | 138.8 | 62.6 | 85.2 / 684.9 / 1,446.0 | 164.2 | 185.6 | 9 | 4,340 / 286 | 0 (0) | 0 | 1.35 | 0 / 0 / 0 / 64.0 |
| 5 | [3mo/128](cells/3mo_m128/) | 128 | 79.2 | 39.0 | 177.6 / 1,933.1 / 4,344.3 | 79.6 | 247.6 | 5 | 3,866 / 542 | 0 (0) | 0 | 2.16 | 0 / 0 / 0 / 64.0 |
| 6 | [3mo/32](cells/3mo_m32/) | 32 | 78.8 | 38.8 | 178.8 / 1,957.2 / 4,337.7 | 124.9 | 247.6 | 17 | 6,151 / 543 | 0 (0) | 0 | 2.17 | 0 / 0 / 0 / 64.0 |
| 7 | [6mo/64](cells/6mo_m64/) | 64 | 138.6 | 62.6 | 85.4 / 689.2 / 1,445.0 | 210.0 | 185.6 | 17 | 5,475 / 286 | 0 (0) | 0 | 1.35 | 0 / 0 / 0 / 64.0 |
| 8 | [6mo/4](cells/6mo_m4/) | 4 | 123.2 | 59.3 | 93.3 / 708.9 / 1,452.2 | 510.9 | 188.4 | 261 | 41,759 / 199 | 1 (3.6) | 1 | 1.42 | 0 / 0 / 0 / 64.0 |
| 9 | [4mo/64](cells/4mo_m64/) | 64 | 91.6 | 45.0 | 149.8 / 1,377.7 / 2,939.7 | 137.0 | 236.8 | 12 | 5,001 / 469 | 0 (0) | 0 | 1.87 | 0 / 0 / 0 / 64.0 |
| 10 | [4mo/4](cells/4mo_m4/) | 4 | 87.0 | 43.8 | 157.3 / 1,421.7 / 3,120.2 | 326.6 | 239.3 | 176 | 34,321 / 492 | 1 (1.9) | 2 | 1.92 | 0 / 0 / 0 / 64.0 |
| 11 | [4mo/32](cells/4mo_m32/) | 32 | 91.0 | 44.9 | 149.4 / 1,380.0 / 2,862.5 | 169.6 | 236.8 | 22 | 6,753 / 469 | 0 (0) | 0 | 1.88 | 0 / 0 / 0 / 64.0 |
| 12 | [3mo/1](cells/3mo_m1/) | 1 | 62.9 | 34.1 | 211.7 / 2,093.0 / 4,524.6 | 343.7 | 249.7 | 526 | 112,951 / 767 | 7 (4.8) | 4 | 2.47 | 0 / 0 / 0 / 64.0 |
| 13 | [4mo/1](cells/4mo_m1/) | 1 | 65.2 | 36.5 | 192.7 / 1,830.2 / 3,908.7 | 468.1 | 239.3 | 696 | 132,808 / 611 | 6 (4.2) | 4 | 2.31 | 0 / 0 / 0 / 64.0 |
| 14 | [3mo/4](cells/3mo_m4/) | 4 | 74.8 | 37.4 | 187.2 / 2,016.9 / 4,422.8 | 238.9 | 248.2 | 132 | 29,267 / 559 | 1 (1.7) | 2 | 2.25 | 0 / 0 / 0 / 64.0 |
| 15 | [4mo/128](cells/4mo_m128/) | 128 | 90.0 | 44.5 | 153.0 / 1,406.6 / 2,957.8 | 109.9 | 236.8 | 7 | 4,122 / 469 | 0 (0) | 0 | 1.89 | 0 / 0 / 0 / 64.0 |
| 16 | 1mo | 4 | running | | | | | | | | | | |
| 17 | 1mo | 1 | pending | | | | | | | | | | |
| 18 | 1mo | 64 | pending | | | | | | | | | | |
| 19 | 1mo | 32 | pending | | | | | | | | | | |
| 20 | 1mo | 128 | pending | | | | | | | | | | |
| 21 | 6mo@W2 | 32 | pending | | | | | | | | | | |
| 22 | 9mo@W2 | 32 | pending | | | | | | | | | | |
| 23 | 9mo@W2 | 64 | pending | | | | | | | | | | |
| 24 | 9mo@W2 | 128 | pending | | | | | | | | | | |
| 25 | 9mo@W2 | 1 | pending | | | | | | | | | | |
| 26 | 9mo@W2 | 4 | pending | | | | | | | | | | |

Data: [`runs.csv`](runs.csv). Each cell folder has `layout_before.md`, `stats.json`, `metrics.md` + `images/`, and logs.

## Geometry (plan estimates; the real boundary is in each cell's `layout_before.md`)

| L | boundary block / step | cold set on HDD (besides 0-8192) | HDD GB | hot steps on SSD | 1-step hot GB |
|---|---|---|---|---|---|
| 6mo | 24,104,000 / 8199 | 8192-8196, 8196-8198 | ~186 | 1,043 | ~730 |
| 4mo | 24,536,000 / ~8543 | 8192-8448, 8448-8512, 8512-8528, +8+4+2+1 | ~225 | ~700 | ~490 |
| 3mo | 24,752,000 / 8714 | 8192-8448, 8448-8704, 8704-8712, 8712-8714 | ~248 | 528 | ~370 |
| 1mo | 25,184,000 / ~9066 | 8192-8448, 8448-8704, 8704-8960, 8960-9024, 9024-9056, +8+2 | ~290 | ~176 | ~125 |
