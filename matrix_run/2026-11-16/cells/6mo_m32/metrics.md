# 6mo_m32

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_6mo_m32` |
| commit | `c604cf14` |
| metrics run label | `mx_6mo_m32_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-11-16T12:14:27Z → 2026-11-16T13:35:20Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=32 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_6mo_m32/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 1.35 h |
| blocks per second (mean) | 2.06 |
| Mgas/s per block mean / p50 / p5 | 138.09 / 133.63 / 36.73 |
| Mgas/s wall clock (all-in) | 62.51 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 202.2 ms / 597.6 ms / 929.0 ms / 1.93 s |
| exec time per block (exec + commitment) worst | 5.32 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 332.5 ms ± 24.1 ms (n=159) |
| commitment time per block p50 / p90 / p95 / p99 | 85.6 ms / 389.5 ms / 693.7 ms / 1.46 s |
| commitment time per block worst | 4.10 s |
| commitment time per block mean ± 95% CI (30 s windows) | 196.7 ms ± 20.3 ms (n=159) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 7,752 / 6,413 / 20,870 / 27,882 / 80,376 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 286.06 / 496.55 / 928.88 / 982.92 / 7,368 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 47.21 / 54.97 / 190.89 / 596.66 / 921.28 |
| share of probes on HDD | 3.56% |
| share of lookups that reached HDD | 6.83% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.8 µs / 12.8 ms / 24.1 ms / 74.9 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.8 µs / 6.4 µs / 149.8 µs / 412.1 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 3.98 / 99.63% / 0.00% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 185.62 GB |
| commitment data size on SSD (end) | 264.99 GB |
| commitment index size on SSD (end) | 8.57 GB |
| commitment data + index size, SSD + HDD (end) | 459.18 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,335 / 10,335 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,103,642 / 24,103,642 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,213 |
| hdd reads per block / read bytes per block | 48.09 / 197.04 KB |
| hdd r_await (mean) / utilization (mean) | 24.2 ms / 43.98% |
| ssd reads per block / read bytes per block | 1,225 / 7.42 MB |
| ssd r_await (mean) / utilization (mean) | 151.7 µs / 30.96% |

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
