# baseline_allssd_merged_6mo_w25400000_2026-10-23-1

| | |
|---|---|
| kind | baseline |
| datadir | `/erigon-data/tv2_bl_run` |
| commit | `037cfbb98b` |
| metrics run label | `baseline_merged_ssd_W` (registered before this name was chosen) |
| blocks | 25,400,000 → 25,407,888 |
| time | 2026-10-23T03:45:14Z → 2026-10-23T04:25:19Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=false --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.sync.mode.chaintip --pfb.exec.stop-at-block=25420000 --tiering.lookback-blocks=1296000 --metrics --metrics.addr=127.0.0.1 --metrics.port=6078
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 7,888 |
| wall time | 0.67 h |
| blocks per second (mean) | 3.28 |
| Mgas/s per block p50 / p5 (mean) | 261.75 / 121.23 (266.29) |
| Mgas/s batch gauge (mean) | 258.11 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 106.1 ms / 203.2 ms / 265.1 ms / 399.0 ms |
| exec time per block (exec + commitment) worst | 946.3 ms |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 128.1 ms ± 10.9 ms (n=79) |
| commitment time per block p50 / p90 / p95 / p99 | 25.6 ms / 54.0 ms / 74.2 ms / 139.5 ms |
| commitment time per block worst | 385.3 ms |
| commitment time per block mean ± 95% CI (30 s windows) | 33.8 ms ± 3.8 ms (n=79) |
| ssd probes per block mean (p50 / p90 / p95 / p99) | 5,305 (5,891 / 10,264 / 20,468 / 28,632) |
| hdd probes per block mean (p50 / p90 / p95 / p99) | 0 (0 / 0 / 0 / 0) |
| hdd slow probes per block mean (p50 / p90 / p95 / p99) | 0 (0 / 0 / 0 / 0) |
| share of probes on HDD | 0.00% |
| share of lookups that reached HDD | 0.00% |
| HDD probe latency p50 / p90 / p95 / p99 | — / — / — / — |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 19.1 µs / 194.2 µs / 442.2 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | — / — / — |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment kv bytes on HDD (end) | 0 B |
| commitment kv bytes on SSD (end) | 310.63 GB |
| commitment accessor bytes on SSD (end) | 6.72 GB |
| commitment bytes SSD + HDD (end) | 317.34 GB |
| SSD saved by movement (end) | 0 B |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 20,023 / 20,023 |
| movement lag, copy_pending (blocks: max / end) | 24,091,854 / 24,091,854 |
| HDD end step / SSD start step (end) | 0 / 0 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,020 |
| sda reads per block / read bytes per block | 0 / 0 B |
| sda r_await (mean) / utilization (mean) | — / 0.00% |
| nvme0n1 reads per block / read bytes per block | 1,027 / 5.16 MB |
| nvme0n1 r_await (mean) / utilization (mean) | 146.5 µs / 37.78% |
| free space on / (end) | 574.50 GB |
| free space on /backup (end) | 5.00 TB |

Note: demotion is off in a baseline, so the movement-lag rows (straddling_file, copy_pending) carry no meaning here.

## Marks

- 2026-10-23T03:45:13Z start baseline_allssd_merged_6mo_w25400000_2026-10-23-1
- 2026-10-23T04:25:19Z stop baseline_allssd_merged_6mo_w25400000_2026-10-23-1 rc=0

## Graphs

### Execution block

![Execution block](images/exec_height.png)

### Blocks per second

![Blocks per second](images/blk_s.png)

### Mgas/s

![Mgas/s](images/mgas_s.png)

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

### Commitment bytes per tier

![Commitment bytes per tier](images/commitment_bytes.png)

### SSD saved and duplicate bytes

![SSD saved and duplicate bytes](images/ssd_saved_duplicate.png)

### Cold data still on SSD (commitment)

![Cold data still on SSD (commitment)](images/lag_bytes.png)

### Movement lag behind the cold boundary (commitment)

![Movement lag behind the cold boundary (commitment)](images/lag_blocks.png)

### Tier edges (steps)

![Tier edges (steps)](images/tier_steps.png)

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

### Free space

![Free space](images/fs_free.png)
