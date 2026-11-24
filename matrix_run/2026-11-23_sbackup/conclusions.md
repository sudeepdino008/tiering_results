Cold `.kv` files of each run are on `/sbackup` (sda1: the first 1 TiB of the HDD, the outer edge); the 2026-11-16 W2 cells had them on `/backup` at 1.85–6.0 TB.
Same blocks, binary and flags as the 2026-11-16 W2 cells; only the HDD placement differs.

| Cell | 2026-11-16 Mgas/s (mean / p5) | here Mgas/s (mean / p5) | commit p50 / p95 ms, 2026-11-16 → here |
|---|---|---|---|
| 6mo@W2/32 | 99.2 / 39.3 | 126.1 / 50.8 (+27 %) | 150.7 / 406.3 → 110.9 / 294.2 |
| 6mo@W2/64 | not run | 126.0 / 51.2 | — → 111.0 / 294.1 |
| 9mo@W2/128 | 153.1 / 63.5 | 164.5 / 69.8 (+7 %) | 83.8 / 452.9 → 72.6 / 194.5 |

- Placement on the disk is a large part of the old 6mo@W2 slowdown. 6mo@W2/32 is still below 6mo/32 at W (138): at W2 it does 419 HDD probes per block, at W 286.
- 6mo@W2: M = 32 and M = 64 give the same speed; M = 64 uses 52 GB less SSD (207 vs 259 GB).
- M = 32 / 64 / 128 ≈ 6 / 12 / 23 days at W2 (measured ~1,250 blocks per step).
