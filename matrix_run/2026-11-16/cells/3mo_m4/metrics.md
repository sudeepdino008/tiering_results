# 3mo_m4

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_3mo_m4` |
| commit | `c604cf14` |
| metrics run label | `mx_3mo_m4_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,409,997 |
| time | 2026-11-17T20:01:37Z → 2026-11-17T22:16:53Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=4 --tiering.lookback-blocks=648000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_3mo_m4/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,997 |
| wall time | 2.25 h |
| blocks per second (mean) | 1.23 |
| Mgas/s per block mean / p50 / p5 / p1 | 74.82 / 71.98 / 15.98 / 8.53 |
| Mgas/s wall clock (all-in) | 37.37 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 373.8 ms / 1.41 s / 2.26 s / 4.67 s |
| exec time per block (exec + commitment) worst | 30.14 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 799.4 ms ± 92.9 ms (n=268) |
| commitment time per block p50 / p90 / p95 / p99 | 187.2 ms / 1.16 s / 2.02 s / 4.42 s |
| commitment time per block worst | 29.10 s |
| commitment time per block mean ± 95% CI (30 s windows) | 595.4 ms ± 89.5 ms (n=268) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 29,267 / 21,215 / 79,553 / 99,884 / 266,819 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 559.45 / 596.45 / 2,953 / 6,487 / 9,314 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 95.76 / 64.19 / 529.45 / 775.81 / 972.91 |
| share of probes on HDD | 1.88% |
| share of lookups that reached HDD | 12.15% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 22.3 ms / 56.2 ms / 164.1 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.7 µs / 2.5 µs / 6.5 µs / 296.0 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.35 / 99.42% / 47.18% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 248.21 GB |
| commitment data size on SSD (end) | 238.94 GB |
| commitment index size on SSD (end) | 8.44 GB |
| commitment data + index size, SSD + HDD (end) | 495.59 GB |
| duplicate bytes (max) | 1.62 GB |
| movement lag, straddling_file (blocks: max / end) | 4,511 / 4,511 |
| movement lag, copy_pending (blocks: max / end) | 4,083 / 0 |
| HDD end block / SSD start block (end) | 24,757,472 / 24,757,472 |
| cold merges: count / total seconds / paused seconds | 2.00 / 614.62 s / 300.67 s |
| cold merges: bytes read / written | 8.01 GB / 5.90 GB |
| major page faults per block | 1,358 |
| hdd reads per block / read bytes per block | 104.65 / 937.67 KB |
| hdd r_await (mean) / utilization (mean) | 39.3 ms / 67.46% |
| ssd reads per block / read bytes per block | 1,357 / 7.16 MB |
| ssd r_await (mean) / utilization (mean) | 151.2 µs / 22.48% |

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
