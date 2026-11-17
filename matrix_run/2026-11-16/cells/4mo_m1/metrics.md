# 4mo_m1

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_4mo_m1` |
| commit | `c604cf14` |
| metrics run label | `mx_4mo_m1_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,409,995 |
| time | 2026-11-17T16:48:42Z → 2026-11-17T19:07:18Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=1 --tiering.lookback-blocks=864000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_4mo_m1/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,995 |
| wall time | 2.31 h |
| blocks per second (mean) | 1.20 |
| Mgas/s per block mean / p50 / p5 | 65.16 / 63.31 / 17.21 |
| Mgas/s wall clock (all-in) | 36.48 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 427.5 ms / 1.36 s / 2.16 s / 4.42 s |
| exec time per block (exec + commitment) worst | 9.42 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 737.2 ms ± 41.5 ms (n=276) |
| commitment time per block p50 / p90 / p95 / p99 | 192.7 ms / 1.07 s / 1.83 s / 3.91 s |
| commitment time per block worst | 9.12 s |
| commitment time per block mean ± 95% CI (30 s windows) | 495.1 ms ± 40.2 ms (n=276) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 132,808 / 81,929 / 298,036 / 661,603 / 965,799 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 610.79 / 607.72 / 3,543 / 6,781 / 9,372 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 73.77 / 61.03 / 407.77 / 710.24 / 952.22 |
| share of probes on HDD | 0.46% |
| share of lookups that reached HDD | 9.92% |
| HDD probe latency p50 / p90 / p95 / p99 | 2.0 µs / 8.4 ms / 24.7 ms / 85.6 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 4.8 µs / 13.2 µs / 975.7 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 5.81 / 99.91% / 88.40% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 239.30 GB |
| commitment data size on SSD (end) | 468.11 GB |
| commitment index size on SSD (end) | 10.81 GB |
| commitment data + index size, SSD + HDD (end) | 718.22 GB |
| duplicate bytes (max) | 720.37 MB |
| movement lag, straddling_file (blocks: max / end) | 1,442 / 811 |
| movement lag, copy_pending (blocks: max / end) | 1,445 / 0 |
| HDD end block / SSD start block (end) | 24,545,181 / 24,545,181 |
| cold merges: count / total seconds / paused seconds | 4.00 / 790.96 s / 442.11 s |
| cold merges: bytes read / written | 9.56 GB / 7.17 GB |
| major page faults per block | 1,971 |
| hdd reads per block / read bytes per block | 80.63 / 803.58 KB |
| hdd r_await (mean) / utilization (mean) | 28.3 ms / 57.90% |
| ssd reads per block / read bytes per block | 1,955 / 9.46 MB |
| ssd r_await (mean) / utilization (mean) | 153.9 µs / 26.94% |

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
