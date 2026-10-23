# baseline_allssd_merged_6mo_w25400000_2026-10-23-2

| | |
|---|---|
| kind | baseline |
| datadir | `/erigon-data/tv2_bl_run` |
| commit | `037cfbb98b` |
| blocks | 25,400,000 → 25,407,926 |
| time | 2026-10-23T05:12:40Z → 2026-10-23T05:52:46Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.sync.mode.chaintip --pfb.exec.stop-at-block=25420000 --tiering.lookback-blocks=1296000 --metrics --metrics.addr=127.0.0.1 --metrics.port=6078
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 7,926 |
| wall time | 0.67 h |
| blocks per second (mean) | 3.29 |
| Mgas/s per block p50 / p5 (mean) | 268.09 / 126.97 (273.29) |
| Mgas/s batch gauge (mean) | 263.62 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 101.9 ms / 196.6 ms / 249.1 ms / 388.4 ms |
| exec time per block (exec + commitment) worst | 943.0 ms |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 127.6 ms ± 14.0 ms (n=79) |
| commitment time per block p50 / p90 / p95 / p99 | 23.0 ms / 49.9 ms / 73.2 ms / 136.2 ms |
| commitment time per block worst | 385.7 ms |
| commitment time per block mean ± 95% CI (30 s windows) | 32.4 ms ± 4.2 ms (n=79) |
| ssd probes per block mean (p50 / p90 / p95 / p99) | 3,815 (5,493 / 9,624 / 14,448 / 27,551) |
| hdd probes per block mean (p50 / p90 / p95 / p99) | 0 (0 / 0 / 0 / 0) |
| hdd slow probes per block mean (p50 / p90 / p95 / p99) | 0 (0 / 0 / 0 / 0) |
| share of probes on HDD | 0.00% |
| share of lookups that reached HDD | 0.00% |
| HDD probe latency p50 / p90 / p95 / p99 | — / — / — / — |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 141.9 µs / 218.6 µs / 441.2 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | — / — / — |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data bytes on HDD (end) | 0 B |
| commitment data bytes on SSD (end) | 310.63 GB |
| commitment index bytes on SSD (end) | 6.72 GB |
| commitment data + index bytes, SSD + HDD (end) | 317.34 GB |
| SSD saved by movement (end) | 0 B |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 20,047 / 20,047 |
| movement lag, copy_pending (blocks: max / end) | 24,091,854 / 24,091,854 |
| HDD end block / SSD start block (end) | — / — |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,015 |
| hdd reads per block / read bytes per block | 0 / 0 B |
| hdd r_await (mean) / utilization (mean) | — / 0.00% |
| ssd reads per block / read bytes per block | 1,016 / 5.11 MB |
| ssd r_await (mean) / utilization (mean) | 139.9 µs / 36.55% |

## Marks

- 2026-10-23T05:12:40Z start baseline_allssd_merged_6mo_w25400000_2026-10-23-2
- 2026-10-23T05:52:46Z stop baseline_allssd_merged_6mo_w25400000_2026-10-23-2 rc=0

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

### Commitment data bytes per tier

![Commitment data bytes per tier](images/commitment_data_bytes.png)

### Commitment index bytes per tier

![Commitment index bytes per tier](images/commitment_index_bytes.png)

### SSD saved and duplicate bytes

![SSD saved and duplicate bytes](images/ssd_saved_duplicate.png)

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

### Disk read latency (r_await)

![Disk read latency (r_await)](images/disk_r_await.png)

### Disk utilization

![Disk utilization](images/disk_util.png)
