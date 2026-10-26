# demote_tiered_merged_992kblk_w25400000_2026-10-26-1

| | |
|---|---|
| kind | baseline |
| datadir | `/erigon-data/tv2_runM_merged_demote` |
| commit | `005d3099` |
| blocks | 25,400,000 → 25,409,999 |
| time | 2026-10-26T06:13:40Z → 2026-10-26T07:34:08Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.sync.mode.chaintip --pfb.exec.stop-at-block=25410000 --tiering.lookback-blocks=992000 --metrics --metrics.addr=127.0.0.1 --metrics.port=6081 --tiering.cold-dir=/backup/erigon-hdd/tv2_runM_merged_demote/domain --tiering.demote 
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,999 |
| wall time | 1.34 h |
| blocks per second (mean) | 2.07 |
| Mgas/s per block p50 / p5 (mean) | 137.69 / 36.95 (142.15) |
| Mgas/s wall clock (all-in) | 62.86 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 195.7 ms / 599.3 ms / 928.6 ms / 1.94 s |
| exec time per block (exec + commitment) worst | 4.98 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 351.5 ms ± 38.7 ms (n=158) |
| commitment time per block p50 / p90 / p95 / p99 | 81.8 ms / 366.7 ms / 663.5 ms / 1.41 s |
| commitment time per block worst | 3.90 s |
| commitment time per block mean ± 95% CI (30 s windows) | 184.4 ms ± 18.7 ms (n=158) |
| ssd probes per block mean (p50 / p90 / p95 / p99) | 3,694 (5,437 / 9,621 / 14,475 / 27,440) |
| hdd probes per block mean (p50 / p90 / p95 / p99) | 152.45 (121.53 / 836.17 / 925.50 / 996.96) |
| hdd slow probes per block mean (p50 / p90 / p95 / p99) | 47.30 (54.73 / 183.61 / 593.03 / 920.57) |
| share of probes on HDD | 3.96% |
| share of lookups that reached HDD | 8.34% |
| HDD probe latency p50 / p90 / p95 / p99 | 2.4 µs / 24.3 ms / 43.7 ms / 97.5 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 2.0 µs / 111.9 µs / 197.0 µs / 377.2 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 1.74 / 73.71% / 0.00% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 211.52 GB |
| commitment data size on SSD (end) | 95.50 GB |
| commitment index size on SSD (end) | 6.70 GB |
| commitment data + index size, SSD + HDD (end) | 313.72 GB |
| SSD space saved (commitment data on HDD) (end) | 211.52 GB |
| duplicate bytes (max) | 29.57 GB |
| movement lag, straddling_file (blocks: max / end) | 317,003 / 9,119 |
| movement lag, copy_pending (blocks: max / end) | 317,011 / 0 |
| HDD end block / SSD start block (end) | 24,408,865 / 24,408,865 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 963.15 |
| hdd reads per block / read bytes per block | 48.30 / 197.85 KB |
| hdd r_await (mean) / utilization (mean) | 25.6 ms / 45.17% |
| ssd reads per block / read bytes per block | 994.59 / 8.10 MB |
| ssd r_await (mean) / utilization (mean) | 145.7 µs / 29.01% |

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

### Share of probes and lookups on HDD

![Share of probes and lookups on HDD](images/hdd_probe_share.png)

### Slow probes (> 1 ms) per second

![Slow probes (> 1 ms) per second](images/slow_probes.png)

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
