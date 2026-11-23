## Conclusions

- **Lookback sets the speed.** With M ≥ 32: 48 Mgas/s (1mo), 79 (3mo), 91 (4mo), 139 (6mo), 149–153 (9mo@W2); all-SSD is 277.
  A shorter lookback gives more HDD reads per block (HDD probes per block: 1,064 at 1mo/64, 286 at 6mo, 146 at 9mo@W2).
- **M sets the SSD size.** 6mo: 729 → 511 → 265 → 210 → 164 GB for M = 1, 4, 32, 64, 128. Each merged file keeps one copy
  of each changed trie node, so many small files keep many copies.
- **The knee is M = 32.** Above 32, speed changes by ≤ 1 % (9mo@W2: +2.7 % at 128). M = 128 is the best cell for every
  lookback: the least SSD at the same or better speed. Frontier: 1mo/64, 3mo/128, 4mo/128, 6mo/128, 9mo@W2/128.
- **Small M does not pay.** M = 1 costs 50 % of the speed at 6mo and 58 % at 9mo@W2; M = 4 costs 11 % at 6mo and 5–6 % at
  3mo/4mo. At 1mo, M has almost no effect (46.9–48.6), because HDD reads dominate. 1-step files cost a lot of SSD:
  6mo/1 uses 729 GB and 9mo@W2/1 uses 1,073 GB, more than all-SSD (307 / 380 GB).
- **Best trade-off at W:** 6mo/128 uses 46 % less SSD than all-SSD (164 vs 307 GB) at 50 % of its speed.
  At W2, 9mo/128 uses 33 % less (254 vs 380 GB) at 153 Mgas/s.
- **HDD placement changes the W2 numbers.** 6mo@W2/32 (99 Mgas/s) is slower than 6mo/32 at W (138) mainly because its cold
  files are far apart on the HDD (long seeks), not because of the block range. In short tests with the same cold files
  placed close together on the disk, 6mo@W2 gave 137–140 Mgas/s.

Skipped: 1mo/32 and 1mo/128 (1mo is too slow), 9mo@W2/4 (not enough SSD space).

