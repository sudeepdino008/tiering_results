# tiering_results

Erigon state-tiering v2 runs. One folder per run: `<run>/metrics.md`, graphs in `<run>/images/`.

Run name: `<kind>_<tiering>_<commitment files>_<lookback>_<variant>_<YYYY-MM-DD>-<n>`, e.g.
`baseline_allssd_merged_6mo_w25400000_2026-10-23-2` (kind `baseline`|`demote`; tiering `allssd`|`hdd0`|`tiered`;
commitment files `1step`|`merged`). The run name is also the `run` label in the metrics store.
