# tiering_results

Erigon state-tiering v2 run results. One folder per run:

```
<run>/<run>.md
<run>/images/<panel>.png
```

Run name (most distinguishing first):
`<kind>_<tiering>_<commitment files>_<lookback>_<variant>_<YYYY-MM-DD>-<n>`

- kind: `baseline` | `demote`
- tiering: `allssd` | `hdd0` (0-8192 commitment on HDD) | `tiered` (demotion on)
- commitment files: `1step` | `merged`
- lookback: `3d`, `1mo`, ...
- variant: what the iteration changed (`r1`, `cachefix`, ...)
- date + run sequence number on that day (`2026-10-22-1`): last

Block range, flags, datadir, commit and all other details go inside the `.md`.
The folder name is `<run>` from the pattern above.

`<run>` is also the `run` label in the metrics store, unless the `.md` names a different `metrics run label`.
