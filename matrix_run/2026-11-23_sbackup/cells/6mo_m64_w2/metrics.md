# 6mo_m64_w2

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_6mo_m64_w2` |
| commit | `c604cf14` |
| metrics run label | `mx_6mo_m64_w26130000_2026-11-23_sbackup` |
| blocks | 26,130,000 → 26,140,000 |
| time | 2026-11-23T21:13:40Z → 2026-11-23T22:28:17Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=26140000 --tiering.commitment-hot-merge-steps=64 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/sbackup/tv2_mx_6mo_m64_w2/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 1.24 h |
| blocks per second (mean) | 2.23 |
| Mgas/s per block mean / p50 / p5 / p1 | 126.04 / 121.02 / 51.20 / 30.98 |
| Mgas/s wall clock (all-in) | 67.69 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 238.5 ms / 429.4 ms / 575.2 ms / 948.3 ms |
| exec time per block (exec + commitment) worst | 1.84 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 288.4 ms ± 16.4 ms (n=147) |
| commitment time per block p50 / p90 / p95 / p99 | 111.0 ms / 234.1 ms / 294.1 ms / 615.4 ms |
| commitment time per block worst | 1.57 s |
| commitment time per block mean ± 95% CI (30 s windows) | 141.8 ms ± 10.7 ms (n=147) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 3,607 / 5,399 / 9,252 / 9,734 / 21,121 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 418.78 / 552.65 / 945.49 / 994.60 / 7,978 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 42.67 / 55.27 / 96.13 / 275.36 / 855.07 |
| share of probes on HDD | 10.41% |
| share of lookups that reached HDD | 7.21% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.8 µs / 3.0 ms / 19.6 ms / 67.5 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 15.3 µs / 189.0 µs / 413.0 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 6.54 / 99.92% / 96.45% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 261.55 GB |
| commitment data size on SSD (end) | 206.85 GB |
| commitment index size on SSD (end) | 9.06 GB |
| commitment data + index size, SSD + HDD (end) | 477.45 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,910 / 10,910 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,833,066 / 24,833,066 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 862.12 |
| hdd reads per block / read bytes per block | 43.89 / 179.94 KB |
| hdd r_await (mean) / utilization (mean) | 25.8 ms / 37.13% |
| ssd reads per block / read bytes per block | 844.83 / 4.28 MB |
| ssd r_await (mean) / utilization (mean) | 142.5 µs / 26.46% |

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
