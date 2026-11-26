# w2_allssd_r1

| | |
|---|---|
| kind | baseline |
| datadir | `/erigon-data/tv2_bl_run` |
| commit | `f32236ec74` |
| metrics run label | `baseline_allssd_w2_f32236ec74_w2_allssd_r1_10000b_w26130000_2026-11-26` |
| blocks | 26,130,000 → 26,140,000 |
| time | 2026-11-26T07:03:45Z → 2026-11-26T07:43:54Z |

Flags:

```
KV_READ_METRICS=false --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.sync.mode.chaintip --pfb.exec.stop-at-block=26140000 --tiering.lookback-blocks=1296000 --metrics --metrics.addr=127.0.0.1 --metrics.port=6078
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 0.67 h |
| blocks per second (mean) | 4.15 |
| Mgas/s per block mean / p50 / p5 / p1 | 251.56 / 248.59 / 125.56 / 88 |
| Mgas/s wall clock (all-in) | 125.90 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 119.1 ms / 219.7 ms / 262.0 ms / 384.2 ms |
| exec time per block (exec + commitment) worst | 801.4 ms |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 132.0 ms ± 4.6 ms (n=78) |
| commitment time per block p50 / p90 / p95 / p99 | 18.2 ms / 33.5 ms / 42.2 ms / 49.1 ms |
| commitment time per block worst | 156.8 ms |
| commitment time per block mean ± 95% CI (30 s windows) | 18.6 ms ± 284.1 µs (n=78) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 2,606 / 5,050 / 9,063 / 9,565 / 9,966 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 0 / 0 / 0 / 0 / 0 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 0 / 0 / 0 / 0 / 0 |
| share of probes on HDD | 0.00% |
| share of lookups that reached HDD | 0.00% |
| HDD probe latency p50 / p90 / p95 / p99 | — / — / — / — |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 0.9 µs / 174.0 µs / 289.6 µs / 689.2 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | — / — / — |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 0 B |
| commitment data size on SSD (end) | 383.86 GB |
| commitment index size on SSD (end) | 7.97 GB |
| commitment data + index size, SSD + HDD (end) | 391.83 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 103,228 / 103,228 |
| movement lag, copy_pending (blocks: max / end) | 24,740,739 / 24,740,739 |
| HDD end block / SSD start block (end) | 0 / 0 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 857.70 |
| hdd reads per block / read bytes per block | 0 / 0 B |
| hdd r_await (mean) / utilization (mean) | — / 0.33% |
| ssd reads per block / read bytes per block | 872.29 / 4.66 MB |
| ssd r_await (mean) / utilization (mean) | 192.0 µs / 29.53% |

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
