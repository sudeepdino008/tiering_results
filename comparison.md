# Comparisons

| A | B | major result | report | gist |
|---|---|---|---|---|
| baseline_allssd_merged_6mo_w25400000_2026-10-23-3 | demote_tiered_1step_6mo_w25400000_2026-10-26-1 | 1-step files on SSD add latency (Mgas/s per block 277 → 69, commitment p50 22 → 154 ms) and size (SSD 312 → 729 GB, ~6x the merged 120 GB) | [metrics.md](cmp_baseline_allssd_merged_6mo_w25400000_2026-10-23-3__demote_tiered_1step_6mo_w25400000_2026-10-26-1/metrics.md) | [gist](https://gist.github.com/sudeepdino008/a44c7188d509cafdbc1d7308d205ae67) |
