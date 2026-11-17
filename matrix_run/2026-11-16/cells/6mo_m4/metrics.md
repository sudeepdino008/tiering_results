# 6mo_m4

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_6mo_m4` |
| commit | `c604cf14` |
| metrics run label | `mx_6mo_m4_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-11-17T03:39:02Z → 2026-11-17T05:04:22Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=4 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_6mo_m4/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 1.42 h |
| blocks per second (mean) | 1.95 |
| Mgas/s per block mean / p50 / p5 | 123.15 / 119.19 / 35.32 |
| Mgas/s wall clock (all-in) | 59.27 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 227.5 ms / 652.8 ms / 958.2 ms / 1.99 s |
| exec time per block (exec + commitment) worst | 4.29 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 352.9 ms ± 21.1 ms (n=169) |
| commitment time per block p50 / p90 / p95 / p99 | 93.3 ms / 433.9 ms / 708.9 ms / 1.45 s |
| commitment time per block worst | 3.93 s |
| commitment time per block mean ± 95% CI (30 s windows) | 204.1 ms ± 18.3 ms (n=169) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 41,759 / 25,959 / 97,351 / 193,803 / 291,009 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 198.63 / 313.48 / 880.50 / 951.38 / 4,268 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 46.41 / 54.55 / 164.53 / 583.52 / 918.72 |
| share of probes on HDD | 0.47% |
| share of lookups that reached HDD | 6.86% |
| HDD probe latency p50 / p90 / p95 / p99 | 2.0 µs / 17.7 ms / 28.7 ms / 79.7 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.8 µs / 3.8 µs / 9.4 µs / 729.9 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 2.75 / 98.92% / 12.07% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 188.40 GB |
| commitment data size on SSD (end) | 510.85 GB |
| commitment index size on SSD (end) | 10.52 GB |
| commitment data + index size, SSD + HDD (end) | 709.77 GB |
| duplicate bytes (max) | 3.24 GB |
| movement lag, straddling_file (blocks: max / end) | 6,956 / 1,850 |
| movement lag, copy_pending (blocks: max / end) | 6,956 / 0 |
| HDD end block / SSD start block (end) | 24,112,148 / 24,112,148 |
| cold merges: count / total seconds / paused seconds | 1.00 / 265.70 s / 51.82 s |
| cold merges: bytes read / written | 6.08 GB / 4.34 GB |
| major page faults per block | 1,509 |
| hdd reads per block / read bytes per block | 52.10 / 711.91 KB |
| hdd r_await (mean) / utilization (mean) | 19.6 ms / 43.36% |
| ssd reads per block / read bytes per block | 1,507 / 7.74 MB |
| ssd r_await (mean) / utilization (mean) | 147.1 µs / 32.24% |

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
