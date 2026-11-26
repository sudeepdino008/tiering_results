# w2_m128_r3

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_pf_6mo_m128_w2_w2_m128_r3` |
| commit | `f32236ec` |
| metrics run label | `pf_6mo_m128_w2_w2_m128_r3_10000b_w26130000_2026-11-26` |
| blocks | 26,130,000 → 26,139,993 |
| time | 2026-11-26T20:44:16Z → 2026-11-26T21:39:44Z |

Flags:

```
KV_READ_METRICS=false --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=26140000 --tiering.commitment-hot-merge-steps=128 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/sbackup/tv2_pf_6mo_m128_w2_w2_m128_r3/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50  --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,993 |
| wall time | 0.92 h |
| blocks per second (mean) | 3.00 |
| Mgas/s per block mean / p50 / p5 / p1 | 152.53 / 147.13 / 62.60 / 41.39 |
| Mgas/s wall clock (all-in) | 91.13 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 194.0 ms / 374.6 ms / 478.6 ms / 837.8 ms |
| exec time per block (exec + commitment) worst | 1.49 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 240.5 ms ± 16.6 ms (n=108) |
| commitment time per block p50 / p90 / p95 / p99 | 18.3 ms / 32.6 ms / 41.6 ms / 48.8 ms |
| commitment time per block worst | 170.0 ms |
| commitment time per block mean ± 95% CI (30 s windows) | 19.0 ms ± 282.6 µs (n=108) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 2,870 / 5,192 / 9,115 / 9,605 / 9,997 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 423.52 / 555.39 / 950.81 / 1,042 / 8,208 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 48.29 / 57.07 / 97.44 / 397.21 / 879.44 |
| share of probes on HDD | 12.86% |
| share of lookups that reached HDD | 7.64% |
| HDD probe latency p50 / p90 / p95 / p99 | 0.7 µs / 7.9 ms / 33.4 ms / 96.4 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 0.8 µs / 128.3 µs / 225.9 µs / 488.9 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 6.46 / 99.91% / 95.27% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 261.55 GB |
| commitment data size on SSD (end) | 168.71 GB |
| commitment index size on SSD (end) | 8.56 GB |
| commitment data + index size, SSD + HDD (end) | 438.82 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,909 / 10,909 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,833,066 / 24,833,066 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 835.71 |
| hdd reads per block / read bytes per block | 43.97 / 180.33 KB |
| hdd r_await (mean) / utilization (mean) | 37.8 ms / 40.22% |
| ssd reads per block / read bytes per block | 839.89 / 4.55 MB |
| ssd r_await (mean) / utilization (mean) | 185.0 µs / 28.58% |

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
