# 6mo_m1

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_6mo_m1` |
| commit | `c604cf14` |
| metrics run label | `mx_6mo_m1_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,409,992 |
| time | 2026-11-16T09:08:54Z → 2026-11-16T11:22:45Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=1 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_6mo_m1/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,992 |
| wall time | 2.23 h |
| blocks per second (mean) | 1.24 |
| Mgas/s per block mean / p50 / p5 / p1 | 69.21 / 67.20 / 18.22 / 10.83 |
| Mgas/s wall clock (all-in) | 37.78 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 399.7 ms / 1.32 s / 2.10 s / 4.37 s |
| exec time per block (exec + commitment) worst | 10.34 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 711.7 ms ± 42.0 ms (n=265) |
| commitment time per block p50 / p90 / p95 / p99 | 155.6 ms / 980.1 ms / 1.73 s / 3.80 s |
| commitment time per block worst | 10.04 s |
| commitment time per block mean ± 95% CI (30 s windows) | 453.7 ms ± 41.0 ms (n=265) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 162,433 / 98,790 / 456,038 / 757,261 / 998,239 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 278.28 / 483.76 / 927.58 / 983.05 / 7,408 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 45.75 / 54.43 / 158.14 / 580.34 / 918.10 |
| share of probes on HDD | 0.17% |
| share of lookups that reached HDD | 6.83% |
| HDD probe latency p50 / p90 / p95 / p99 | 2.1 µs / 8.3 ms / 16.6 ms / 30.8 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 6.5 µs / 22.8 µs / 1.5 ms |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 3.85 / 99.71% / 24.12% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 189.28 GB |
| commitment data size on SSD (end) | 729.37 GB |
| commitment index size on SSD (end) | 12.93 GB |
| commitment data + index size, SSD + HDD (end) | 931.58 GB |
| duplicate bytes (max) | 1.52 GB |
| movement lag, straddling_file (blocks: max / end) | 1,941 / 330 |
| movement lag, copy_pending (blocks: max / end) | 1,952 / 0 |
| HDD end block / SSD start block (end) | 24,113,651 / 24,113,651 |
| cold merges: count / total seconds / paused seconds | 3.00 / 847.61 s / 393.01 s |
| cold merges: bytes read / written | 13.07 GB / 9.86 GB |
| major page faults per block | 2,307 |
| hdd reads per block / read bytes per block | 56.07 / 1.14 MB |
| hdd r_await (mean) / utilization (mean) | 10.2 ms / 38.01% |
| ssd reads per block / read bytes per block | 2,294 / 11.34 MB |
| ssd r_await (mean) / utilization (mean) | 154.6 µs / 28.74% |

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
