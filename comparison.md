# Comparisons

## Major results

- 1-step files on SSD add latency (Mgas/s per block 277 → 69, commitment p50 22 → 154 ms) and size (SSD 312 → 729 GB,
  ~6x the merged 120 GB). Source: baseline vs 2c below.
- A big demotion copy slows blocks: run M (merged files, demotion on) copied the 28.9 GB 8192-8448 file in 163 s; Mgas/s
  fell 139 → 74 during the copy. The pause gate covers only the commitment computation; the loss is in execution
  (block 1.14 s vs 0.29 s). Guess: the copy evicts hot pages from the page cache. Not saved as a report.

## Reports

| A | B | report | gist |
|---|---|---|---|
| baseline_allssd_merged_6mo_w25400000_2026-10-23-3 | demote_tiered_1step_6mo_w25400000_2026-10-26-1 | [metrics.md](cmp_baseline_allssd_merged_6mo_w25400000_2026-10-23-3__demote_tiered_1step_6mo_w25400000_2026-10-26-1/metrics.md) | [gist](https://gist.github.com/sudeepdino008/a44c7188d509cafdbc1d7308d205ae67) |
