# tiering_results

Erigon state-tiering v2 runs. One folder per run: `<run>/metrics.md`, graphs in `<run>/images/`.

Run name: `<kind>_<tiering>_<commitment files>_<lookback>_<variant>_<YYYY-MM-DD>-<n>`, e.g.
`baseline_allssd_merged_6mo_w25400000_2026-10-23-2` (kind `baseline`|`demote`; tiering `allssd`|`hdd0`|`tiered`;
commitment files `1step`|`merged`). The run name is also the `run` label in the metrics store.

### Note about the tiering runs:

- the runs start from `W = 25400000` (June 26, 2026)
- all runs execute 10k blocks (in today's erigon it takes about 40 minutes) -- this has shown to stabilize the perf numbers while proving enough room for demotions AND merge of HDD files to take place.
- 10k blocks should produce 6 commitment files, and we should see demotions of approximately as many files in that 40 minute period. We should also see merges happening in HDD.
