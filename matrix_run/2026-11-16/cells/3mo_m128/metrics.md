# 3mo_m128

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_3mo_m128` |
| commit | `c604cf14` |
| metrics run label | `mx_3mo_m128_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-11-16T19:25:57Z → 2026-11-16T21:35:45Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=128 --tiering.lookback-blocks=648000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_3mo_m128/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 2.16 h |
| blocks per second (mean) | 1.28 |
| Mgas/s per block mean / p50 / p5 / p1 | 79.25 / 76.02 / 16.86 / 9.36 |
| Mgas/s wall clock (all-in) | 38.95 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 355.7 ms / 1.33 s / 2.18 s / 4.58 s |
| exec time per block (exec + commitment) worst | 10.73 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 729.5 ms ± 50.9 ms (n=258) |
| commitment time per block p50 / p90 / p95 / p99 | 177.6 ms / 1.10 s / 1.93 s / 4.34 s |
| commitment time per block worst | 10.47 s |
| commitment time per block mean ± 95% CI (30 s windows) | 531.7 ms ± 47.7 ms (n=258) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 3,866 / 5,514 / 9,693 / 16,131 / 28,036 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 542.37 / 595.75 / 2,797 / 6,406 / 9,293 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 95.62 / 64.32 / 533.17 / 777.07 / 972.20 |
| share of probes on HDD | 12.30% |
| share of lookups that reached HDD | 12.11% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 23.1 ms / 57.5 ms / 162.9 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 2.0 µs / 101.9 µs / 200.4 µs / 410.8 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.24 / 99.90% / 55.37% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 247.59 GB |
| commitment data size on SSD (end) | 79.62 GB |
| commitment index size on SSD (end) | 6.95 GB |
| commitment data + index size, SSD + HDD (end) | 334.17 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,725 / 10,725 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,751,258 / 24,751,258 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,088 |
| hdd reads per block / read bytes per block | 99.78 / 408.81 KB |
| hdd r_await (mean) / utilization (mean) | 40.4 ms / 66.21% |
| ssd reads per block / read bytes per block | 1,074 / 6.28 MB |
| ssd r_await (mean) / utilization (mean) | 161.6 µs / 20.93% |

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
