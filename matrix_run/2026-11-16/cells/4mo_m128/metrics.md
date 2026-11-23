# 4mo_m128

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_4mo_m128` |
| commit | `c604cf14` |
| metrics run label | `mx_4mo_m128_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,409,988 |
| time | 2026-11-17T23:06:06Z → 2026-11-18T00:59:46Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=128 --tiering.lookback-blocks=864000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_4mo_m128/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,988 |
| wall time | 1.89 h |
| blocks per second (mean) | 1.46 |
| Mgas/s per block mean / p50 / p5 / p1 | 90.02 / 86.26 / 20.49 / 11.61 |
| Mgas/s wall clock (all-in) | 44.48 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 311.5 ms / 1.07 s / 1.82 s / 3.83 s |
| exec time per block (exec + commitment) worst | 8.23 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 576.2 ms ± 39.6 ms (n=225) |
| commitment time per block p50 / p90 / p95 / p99 | 153.0 ms / 835.8 ms / 1.41 s / 2.96 s |
| commitment time per block worst | 7.97 s |
| commitment time per block mean ± 95% CI (30 s windows) | 401.9 ms ± 37.3 ms (n=225) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 4,122 / 5,602 / 9,774 / 17,648 / 28,461 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 468.94 / 575.53 / 999.70 / 5,487 / 9,097 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 73.68 / 61.45 / 437.90 / 723.82 / 952.55 |
| share of probes on HDD | 10.21% |
| share of lookups that reached HDD | 9.91% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 19.1 ms / 46.9 ms / 143.7 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 104.0 µs / 201.6 µs / 414.5 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.48 / 99.95% / 67.70% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 236.84 GB |
| commitment data size on SSD (end) | 109.91 GB |
| commitment index size on SSD (end) | 7.22 GB |
| commitment data + index size, SSD + HDD (end) | 353.97 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,052 / 10,052 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,535,923 / 24,535,923 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,124 |
| hdd reads per block / read bytes per block | 76.23 / 312.43 KB |
| hdd r_await (mean) / utilization (mean) | 38.9 ms / 61.15% |
| ssd reads per block / read bytes per block | 1,134 / 6.95 MB |
| ssd r_await (mean) / utilization (mean) | 155.5 µs / 23.38% |

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
