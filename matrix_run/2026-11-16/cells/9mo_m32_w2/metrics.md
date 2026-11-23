# 9mo_m32_w2

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_9mo_m32_w2` |
| commit | `c604cf14` |
| metrics run label | `mx_9mo_m32_w26130000_2026-11-16` |
| blocks | 26,130,000 → 26,139,997 |
| time | 2026-11-19T09:09:45Z → 2026-11-19T10:16:42Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=26140000 --tiering.commitment-hot-merge-steps=32 --tiering.lookback-blocks=1944000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_9mo_m32_w2/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,997 |
| wall time | 1.12 h |
| blocks per second (mean) | 2.49 |
| Mgas/s per block mean / p50 / p5 / p1 | 149.13 / 142.67 / 61.42 / 37.59 |
| Mgas/s wall clock (all-in) | 75.48 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 203.0 ms / 366.5 ms / 456.0 ms / 749.1 ms |
| exec time per block (exec + commitment) worst | 1.55 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 238.1 ms ± 13.0 ms (n=131) |
| commitment time per block p50 / p90 / p95 / p99 | 87.4 ms / 187.3 ms / 235.7 ms / 469.4 ms |
| commitment time per block worst | 1.33 s |
| commitment time per block mean ± 95% CI (30 s windows) | 111.5 ms ± 9.1 ms (n=131) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 6,157 / 5,952 / 10,832 / 20,662 / 28,526 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 146.23 / 331.83 / 867.22 / 934.15 / 987.69 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 27.89 / 48.44 / 92.07 / 97.52 / 670.43 |
| share of probes on HDD | 2.32% |
| share of lookups that reached HDD | 5.56% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 17.9 ms / 33.1 ms / 84.9 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.8 µs / 5.4 µs / 133.1 µs / 413.6 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 2.96 / 99.95% / 0.00% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 196.31 GB |
| commitment data size on SSD (end) | 396.70 GB |
| commitment index size on SSD (end) | 10.70 GB |
| commitment data + index size, SSD + HDD (end) | 603.71 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,817 / 10,817 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,185,177 / 24,185,177 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 908.80 |
| hdd reads per block / read bytes per block | 28.85 / 118.29 KB |
| hdd r_await (mean) / utilization (mean) | 24.9 ms / 39.55% |
| ssd reads per block / read bytes per block | 908.50 / 4.71 MB |
| ssd r_await (mean) / utilization (mean) | 139.8 µs / 28.63% |

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
