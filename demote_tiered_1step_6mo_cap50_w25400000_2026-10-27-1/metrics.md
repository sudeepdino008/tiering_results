# demote_tiered_1step_6mo_cap50_w25400000_2026-10-27-1

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_run16a_6mo` |
| commit | `b9bd13f0` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-10-27T09:12:50Z → 2026-10-27T11:28:15Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=1 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/backup/erigon-hdd/tv2_run16a_6mo/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.demote-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

Notes come from `notes.json` (metric name -> note) in this folder.

| Metric | Value | Notes |
|---|---|---|
| blocks executed | 10,000 |  |
| wall time | 2.26 h |  |
| blocks per second (mean) | 1.23 |  |
| Mgas/s per block mean / p50 / p5 | 68.92 / 66.97 / 17.92 |  |
| Mgas/s wall clock (all-in) | 37.35 |  |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 402.9 ms / 1.34 s / 2.12 s / 4.42 s |  |
| exec time per block (exec + commitment) worst | 10.69 s |  |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 711.6 ms ± 41.4 ms (n=268) |  |
| commitment time per block p50 / p90 / p95 / p99 | 154.0 ms / 991.5 ms / 1.76 s / 3.79 s |  |
| commitment time per block worst | 10.42 s |  |
| commitment time per block mean ± 95% CI (30 s windows) | 452.5 ms ± 41.3 ms (n=268) |  |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 162,356 / 98,836 / 454,616 / 756,601 / 998,188 |  |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 265.50 / 468.02 / 922.51 / 979.32 / 7,170 |  |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 43.65 / 53.71 / 121.16 / 561.90 / 914.50 |  |
| share of probes on HDD | 0.16% |  |
| share of lookups that reached HDD | 6.85% |  |
| HDD probe latency p50 / p90 / p95 / p99 | 2.1 µs / 7.7 ms / 14.6 ms / 24.5 ms |  |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 7.5 µs / 36.4 µs / 1.6 ms |  |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 3.67 / 99.65% / 17.27% |  |
| existence-filter false positives (HDD / SSD) | 0 / 0 |  |
| commitment data size on HDD (end) | 189.28 GB |  |
| commitment data size on SSD (end) | 729.37 GB |  |
| commitment index size on SSD (end) | 12.93 GB |  |
| commitment data + index size, SSD + HDD (end) | 931.58 GB |  |
| SSD space saved (commitment data on HDD) (end) | 189.28 GB |  |
| duplicate bytes (max) | 1.54 GB |  |
| movement lag, straddling_file (blocks: max / end) | 1,941 / 342 |  |
| movement lag, copy_pending (blocks: max / end) | 1,952 / 0 |  |
| HDD end block / SSD start block (end) | 24,113,651 / 24,113,651 |  |
| cold merges: count / total seconds / paused seconds | 3.00 / 132.03 s / 29.81 s | merges not rate-capped: wall Mgas/s during merges 31.8 vs 39.5 around (-19%, same in 2c) |
| cold merges: bytes read / written | 13.07 GB / 9.85 GB |  |
| major page faults per block | 1,659 |  |
| hdd reads per block / read bytes per block | 50.62 / 705.88 KB |  |
| hdd r_await (mean) / utilization (mean) | 10.3 ms / 35.07% | copy cap 50 MB/s: HDD fault latency during copies 14.2 ms vs 10.2 around (1.4x); 2c no cap: 147 vs 10.3 ms (14x). Wall Mgas/s during copies 38.8 vs 39.5 around (2c: 34.8 vs 39.4). rate limiter works |
| ssd reads per block / read bytes per block | 1,630 / 8.48 MB |  |
| ssd r_await (mean) / utilization (mean) | 160.1 µs / 25.19% |  |

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
