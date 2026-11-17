# 3mo_m1

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_3mo_m1` |
| commit | `c604cf14` |
| metrics run label | `mx_3mo_m1_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-11-17T13:55:21Z → 2026-11-17T16:23:46Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=1 --tiering.lookback-blocks=648000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_3mo_m1/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 2.47 h |
| blocks per second (mean) | 1.12 |
| Mgas/s per block mean / p50 / p5 | 62.89 / 60.96 / 15.21 |
| Mgas/s wall clock (all-in) | 34.07 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 442.4 ms / 1.52 s / 2.37 s / 4.75 s |
| exec time per block (exec + commitment) worst | 23.20 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 854.6 ms ± 66.0 ms (n=294) |
| commitment time per block p50 / p90 / p95 / p99 | 211.7 ms / 1.23 s / 2.09 s / 4.52 s |
| commitment time per block worst | 22.71 s |
| commitment time per block mean ± 95% CI (30 s windows) | 610.9 ms ± 62.4 ms (n=294) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 112,951 / 75,033 / 278,568 / 572,787 / 942,668 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 766.68 / 637.21 / 4,980 / 7,531 / 9,571 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 96.47 / 64.23 / 528.24 / 775.49 / 973.30 |
| share of probes on HDD | 0.67% |
| share of lookups that reached HDD | 12.14% |
| HDD probe latency p50 / p90 / p95 / p99 | 2.0 µs / 10.4 ms / 34.3 ms / 100.7 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.8 µs / 3.2 µs / 8.4 µs / 554.1 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 5.95 / 99.88% / 83.89% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 249.67 GB |
| commitment data size on SSD (end) | 343.73 GB |
| commitment index size on SSD (end) | 9.62 GB |
| commitment data + index size, SSD + HDD (end) | 603.01 GB |
| duplicate bytes (max) | 809.50 MB |
| movement lag, straddling_file (blocks: max / end) | 1,859 / 1,358 |
| movement lag, copy_pending (blocks: max / end) | 1,860 / 0 |
| HDD end block / SSD start block (end) | 24,760,633 / 24,760,633 |
| cold merges: count / total seconds / paused seconds | 4.00 / 876.39 s / 424.57 s |
| cold merges: bytes read / written | 11.76 GB / 8.43 GB |
| major page faults per block | 1,838 |
| hdd reads per block / read bytes per block | 107.43 / 1.21 MB |
| hdd r_await (mean) / utilization (mean) | 34.6 ms / 65.23% |
| ssd reads per block / read bytes per block | 1,817 / 9.09 MB |
| ssd r_await (mean) / utilization (mean) | 154.3 µs / 25.26% |

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
