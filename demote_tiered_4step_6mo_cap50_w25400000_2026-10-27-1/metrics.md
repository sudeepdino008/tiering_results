# demote_tiered_4step_6mo_cap50_w25400000_2026-10-27-1

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_run16b_6mo` |
| commit | `c604cf14` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-10-27T12:31:04Z → 2026-10-27T13:54:05Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=4 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/backup/erigon-hdd/tv2_run16b_6mo/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

Notes come from `notes.json` (metric name -> note) in this folder.

| Metric | Value | Notes |
|---|---|---|
| blocks executed | 10,000 |  |
| wall time | 1.38 h |  |
| blocks per second (mean) | 2.01 |  |
| Mgas/s per block mean / p50 / p5 | 126.31 / 122.14 / 39.74 |  |
| Mgas/s wall clock (all-in) | 60.92 |  |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 223.3 ms / 610.2 ms / 896.7 ms / 1.54 s |  |
| exec time per block (exec + commitment) worst | 3.55 s |  |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 325.0 ms ± 17.5 ms (n=165) |  |
| commitment time per block p50 / p90 / p95 / p99 | 90.9 ms / 395.9 ms / 657.2 ms / 1.28 s |  |
| commitment time per block worst | 3.29 s |  |
| commitment time per block mean ± 95% CI (30 s windows) | 182.1 ms ± 15.4 ms (n=165) |  |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 41,749 / 25,952 / 97,349 / 193,803 / 291,009 |  |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 198.48 / 311.86 / 880.22 / 951.26 / 4,268 |  |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 44.86 / 54.10 / 136.38 / 569.49 / 915.98 |  |
| share of probes on HDD | 0.47% |  |
| share of lookups that reached HDD | 6.87% |  |
| HDD probe latency p50 / p90 / p95 / p99 | 2.0 µs / 16.7 ms / 26.6 ms / 75.5 ms |  |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.8 µs / 4.3 µs / 9.8 µs / 875.7 µs |  |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 2.75 / 98.92% / 12.02% |  |
| existence-filter false positives (HDD / SSD) | 0 / 0 |  |
| commitment data size on HDD (end) | 188.40 GB |  |
| commitment data size on SSD (end) | 510.85 GB | 4-step merges on SSD: 512 GB at start vs ~720 GB 1-step (0.71x); fully merged would be ~120 GB |
| commitment index size on SSD (end) | 10.52 GB |  |
| commitment data + index size, SSD + HDD (end) | 709.77 GB |  |
| SSD space saved (commitment data on HDD) (end) | 188.40 GB |  |
| duplicate bytes (max) | 3.28 GB |  |
| movement lag, straddling_file (blocks: max / end) | 6,948 / 1,848 |  |
| movement lag, copy_pending (blocks: max / end) | 6,956 / 0 |  |
| HDD end block / SSD start block (end) | 24,112,148 / 24,112,148 |  |
| cold merges: count / total seconds / paused seconds | 1.00 / 262.97 s / 52.06 s | merges capped too (cold-io-max-mbps=50): 8192-8200 took 263 s (16a: 76 s); wall Mgas/s during merge 65.7 vs 68.0 around (-3%; 16a: -19%) |
| cold merges: bytes read / written | 6.08 GB / 4.34 GB |  |
| major page faults per block | 1,138 |  |
| hdd reads per block / read bytes per block | 50.54 / 705.68 KB |  |
| hdd r_await (mean) / utilization (mean) | 18.3 ms / 41.80% | during copies (cap 50): wall Mgas/s 62.5 vs 68.0 around (-8%) |
| ssd reads per block / read bytes per block | 1,129 / 5.92 MB |  |
| ssd r_await (mean) / utilization (mean) | 153.1 µs / 29.86% |  |

## Graphs

### Execution block

![Execution block](images/exec_height.png)

### Blocks per second

![Blocks per second](images/blk_s.png)

### Mgas/s per block

![Mgas/s per block](images/mgas_s.png)

### Exec time per block (exec + commitment)

![Exec time per block (exec + commitment)](images/exec_block_seconds.png)

### Commitment time per block

![Commitment time per block](images/commitment_seconds.png)

### Commitment file probes per block

![Commitment file probes per block](images/probes_per_block.png)

*probe = one file checked during a key lookup, newest file first; more files, more probes per lookup.*

### Share of probes and lookups on HDD

![Share of probes and lookups on HDD](images/hdd_probe_share.png)

*lookup = one commitment key read that missed the state cache and the DB; probe = one file checked in it, newest file first, until the key is found. A lookup reaches HDD when no SSD file has the key.*

### Slow probes (> 1 ms) per second

![Slow probes (> 1 ms) per second](images/slow_probes.png)

*HDD: every probe timed (actual count). SSD: only 1 in 16 lookups timed; the line is that sample x16.*

### HDD probe latency

![HDD probe latency](images/probe_latency_hdd.png)

### SSD probe latency (sampled)

![SSD probe latency (sampled)](images/probe_latency_ssd.png)

### HDD probes per lookup (lookups that reached HDD)

![HDD probes per lookup (lookups that reached HDD)](images/probes_per_lookup_hdd.png)

### Commitment data size per tier

![Commitment data size per tier](images/commitment_data_size.png)

### Commitment index size per tier

![Commitment index size per tier](images/commitment_index_size.png)

### SSD space saved and duplicate size

![SSD space saved and duplicate size](images/ssd_saved_duplicate.png)

### Cold data still on SSD (commitment)

![Cold data still on SSD (commitment)](images/lag_bytes.png)

### Movement lag behind the cold boundary (commitment)

![Movement lag behind the cold boundary (commitment)](images/lag_blocks.png)

### Tier edges (blocks)

![Tier edges (blocks)](images/tier_edges.png)

### Demotions (commitment)

![Demotions (commitment)](images/demotions.png)

### Demoted bytes and copy rate

![Demoted bytes and copy rate](images/demotion_bytes.png)

### Demotion time and pauses

![Demotion time and pauses](images/demotion_seconds.png)

### Cold merges (commitment, HDD)

![Cold merges (commitment, HDD)](images/cold_merge.png)

### Cold merge bytes

![Cold merge bytes](images/cold_merge_bytes.png)

### Major page faults per second

![Major page faults per second](images/major_faults.png)

### Disk reads per second

![Disk reads per second](images/disk_reads.png)

### Disk read bytes per second

![Disk read bytes per second](images/disk_read_bytes.png)

### SSD read latency (r_await)

![SSD read latency (r_await)](images/disk_r_await_ssd.png)

### HDD read latency (r_await)

![HDD read latency (r_await)](images/disk_r_await_hdd.png)

### Disk utilization

![Disk utilization](images/disk_util.png)
