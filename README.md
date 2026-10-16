# tiering_results

Erigon state-tiering v2 run results. Flat layout: one `.md` per run, PNGs next to it with the same prefix.

File name (most distinguishing first):
`<kind>_<tiering>_<commitment files>_<lookback>_<variant>_<YYYY-MM-DD>-<n>.md`

- kind: `baseline` | `demote`
- tiering: `allssd` | `hdd0` (0-8192 commitment on HDD) | `tiered` (demotion on)
- commitment files: `1step` | `merged`
- lookback: `3d`, `1mo`, ...
- variant: what the iteration changed (`r1`, `cachefix`, ...)
- date + run sequence number on that day (`2026-10-22-1`): last

Block range, flags, datadir, commit and all other details go inside the `.md`.

PNG: `<same prefix>_<panel>.png`. The prefix is also the `run` label in the metrics store.
