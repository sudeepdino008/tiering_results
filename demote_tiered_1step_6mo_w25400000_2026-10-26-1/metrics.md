# demote_tiered_1step_6mo_w25400000_2026-10-26-1

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_run_6mo_10k` |
| commit | `005d3099` |
| blocks | 25,400,000 → 25,409,993 |
| time | 2026-10-26T03:57:00Z → 2026-10-26T06:11:30Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=1 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/backup/erigon-hdd/tv2_run_6mo_10k/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,993 |
| wall time | 2.24 h |
| blocks per second (mean) | 1.24 |
| Mgas/s per block mean / p50 / p5 | 69.28 / 67.19 / 17.97 |
| Mgas/s wall clock (all-in) | 37.60 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 400.4 ms / 1.35 s / 2.13 s / 4.40 s |
| exec time per block (exec + commitment) worst | 10.81 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 718.5 ms ± 43.0 ms (n=266) |
| commitment time per block p50 / p90 / p95 / p99 | 154.2 ms / 987.0 ms / 1.73 s / 3.71 s |
| commitment time per block worst | 10.55 s |
| commitment time per block mean ± 95% CI (30 s windows) | 456.5 ms ± 41.7 ms (n=266) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 162,371 / 98,783 / 455,509 / 757,022 / 998,232 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 267.39 / 470.56 / 923.19 / 979.77 / 7,198 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 43.64 / 53.73 / 119.18 / 560.92 / 914.31 |
| share of probes on HDD | 0.16% |
| share of lookups that reached HDD | 6.85% |
| HDD probe latency p50 / p90 / p95 / p99 | 2.2 µs / 7.7 ms / 14.4 ms / 24.4 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 2.0 µs / 7.5 µs / 35.8 µs / 1.6 ms |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 3.70 / 99.65% / 17.95% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 189.28 GB |
| commitment data size on SSD (end) | 729.37 GB |
| commitment index size on SSD (end) | 12.93 GB |
| commitment data + index size, SSD + HDD (end) | 931.58 GB |
| SSD space saved (commitment data on HDD) (end) | 189.28 GB |
| duplicate bytes (max) | 1.14 GB |
| movement lag, straddling_file (blocks: max / end) | 1,941 / 342 |
| movement lag, copy_pending (blocks: max / end) | 1,952 / 0 |
| HDD end block / SSD start block (end) | 24,113,651 / 24,113,651 |
| cold merges: count / total seconds / paused seconds | 3.00 / 122.74 s / 26.09 s |
| cold merges: bytes read / written | 13.08 GB / 9.86 GB |
| major page faults per block | 1,659 |
| hdd reads per block / read bytes per block | 50.64 / 705.93 KB |
| hdd r_await (mean) / utilization (mean) | 10.4 ms / 35.10% |
| ssd reads per block / read bytes per block | 1,630 / 8.47 MB |
| ssd r_await (mean) / utilization (mean) | 158.7 µs / 24.84% |

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
