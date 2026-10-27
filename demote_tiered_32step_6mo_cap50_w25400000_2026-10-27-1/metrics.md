# demote_tiered_32step_6mo_cap50_w25400000_2026-10-27-1

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_run16c_6mo` |
| commit | `c604cf14` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-10-27T16:48:46Z → 2026-10-27T18:08:42Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=32 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/backup/erigon-hdd/tv2_run16c_6mo/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

Notes come from `notes.json` (metric name -> note) in this folder.

| Metric | Value | Notes |
|---|---|---|
| blocks executed | 10,000 |  |
| wall time | 1.33 h |  |
| blocks per second (mean) | 2.08 |  |
| Mgas/s per block mean / p50 / p5 | 140.09 / 135.45 / 38.76 |  |
| Mgas/s wall clock (all-in) | 63.29 |  |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 198.6 ms / 578.4 ms / 898.1 ms / 1.76 s |  |
| exec time per block (exec + commitment) worst | 4.50 s |  |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 316.6 ms ± 21.3 ms (n=157) |  |
| commitment time per block p50 / p90 / p95 / p99 | 84.7 ms / 385.7 ms / 679.4 ms / 1.42 s |  |
| commitment time per block worst | 4.20 s |  |
| commitment time per block mean ± 95% CI (30 s windows) | 188.5 ms ± 19.3 ms (n=157) |  |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 7,744 / 6,411 / 20,857 / 27,879 / 80,376 |  |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 286.09 / 496.43 / 928.86 / 982.92 / 7,368 |  |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 46.72 / 54.81 / 187.96 / 595.20 / 921.00 |  |
| share of probes on HDD | 3.56% |  |
| share of lookups that reached HDD | 6.85% |  |
| HDD probe latency p50 / p90 / p95 / p99 | 1.8 µs / 12.5 ms / 24.0 ms / 74.5 ms |  |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.8 µs / 5.8 µs / 125.3 µs / 360.0 µs |  |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 3.98 / 99.63% / 0.00% |  |
| existence-filter false positives (HDD / SSD) | 0 / 0 |  |
| commitment data size on HDD (end) | 185.62 GB |  |
| commitment data size on SSD (end) | 264.99 GB | 32-step merges on SSD: 265 GB (16b 4-step 511, 2c 1-step 729, baseline merged 312) |
| commitment index size on SSD (end) | 8.57 GB |  |
| commitment data + index size, SSD + HDD (end) | 459.18 GB |  |
| SSD space saved (commitment data on HDD) (end) | 185.62 GB |  |
| duplicate bytes (max) | 0 B |  |
| movement lag, straddling_file (blocks: max / end) | 10,338 / 10,338 |  |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 | no demotion: a 32-step file goes cold only when its whole range is past the boundary; the run moves it ~1.4 steps |
| HDD end block / SSD start block (end) | 24,103,642 / 24,103,642 |  |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |  |
| cold merges: bytes read / written | 0 B / 0 B |  |
| major page faults per block | 938.86 |  |
| hdd reads per block / read bytes per block | 47.59 / 195.00 KB |  |
| hdd r_await (mean) / utilization (mean) | 24.3 ms / 43.94% |  |
| ssd reads per block / read bytes per block | 947.99 / 4.80 MB |  |
| ssd r_await (mean) / utilization (mean) | 146.6 µs / 28.53% |  |

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
