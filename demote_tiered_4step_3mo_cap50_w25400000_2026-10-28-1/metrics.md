# demote_tiered_4step_3mo_cap50_w25400000_2026-10-28-1

3mo lookback (648,000 blocks) + 4-step = SSD commitment files merged up to 4 steps ≈ 1 day of chain (1 step = 390,625 txns ≈ 1,700 blocks ≈ 5.7 h at the chain tip). Cold files were merged on SSD in prep, then moved to HDD.

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_run16d_3mo` |
| commit | `c604cf14` |
| blocks | 25,400,000 → 25,409,988 |
| time | 2026-10-28T11:38:27Z → 2026-10-28T13:47:37Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=4 --tiering.lookback-blocks=648000 --tiering.cold-dir=/backup/erigon-hdd/tv2_run16d_3mo/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

Notes come from `notes.json` (metric name -> note) in this folder.

| Metric | Value | Notes |
|---|---|---|
| blocks executed | 9,988 |  |
| wall time | 2.15 h |  |
| blocks per second (mean) | 1.29 |  |
| Mgas/s per block mean / p50 / p5 | 78.82 / 75.60 / 17.03 |  |
| Mgas/s wall clock (all-in) | 39.14 |  |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 357.6 ms / 1.31 s / 2.16 s / 4.54 s |  |
| exec time per block (exec + commitment) worst | 20.90 s |  |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 724.2 ms ± 69.1 ms (n=257) |  |
| commitment time per block p50 / p90 / p95 / p99 | 179.1 ms / 1.09 s / 1.93 s / 4.32 s |  |
| commitment time per block worst | 20.65 s |  |
| commitment time per block mean ± 95% CI (30 s windows) | 530.6 ms ± 64.3 ms (n=257) |  |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 29,267 / 21,197 / 79,506 / 99,902 / 266,857 |  |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 559.75 / 596.60 / 2,960 / 6,490 / 9,315 | 3mo puts 3-6mo old data on HDD: 2.8x the HDD probes of 16b (6mo, 4-step) |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 93.86 / 64.09 / 526.08 / 773.44 / 971.33 |  |
| share of probes on HDD | 1.88% |  |
| share of lookups that reached HDD | 12.17% |  |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 21.0 ms / 52.0 ms / 153.4 ms |  |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.7 µs / 2.5 µs / 6.3 µs / 239.1 µs |  |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.35 / 99.43% / 47.27% |  |
| existence-filter false positives (HDD / SSD) | 0 / 0 |  |
| commitment data size on HDD (end) | 248.21 GB |  |
| commitment data size on SSD (end) | 238.94 GB | 4-step, 3mo hot: 239 GB (16b 6mo hot: 511 GB) |
| commitment index size on SSD (end) | 8.44 GB |  |
| commitment data + index size, SSD + HDD (end) | 495.59 GB |  |
| SSD space saved (commitment data on HDD) (end) | 248.21 GB |  |
| duplicate bytes (max) | 1.56 GB |  |
| movement lag, straddling_file (blocks: max / end) | 4,513 / 4,513 |  |
| movement lag, copy_pending (blocks: max / end) | 4,083 / 0 |  |
| HDD end block / SSD start block (end) | 24,757,472 / 24,757,472 |  |
| cold merges: count / total seconds / paused seconds | 2.00 / 577.23 s / 279.45 s |  |
| cold merges: bytes read / written | 8.02 GB / 5.91 GB |  |
| major page faults per block | 994.99 |  |
| hdd reads per block / read bytes per block | 101.88 / 763.27 KB |  |
| hdd r_await (mean) / utilization (mean) | 38.2 ms / 66.63% |  |
| ssd reads per block / read bytes per block | 961.94 / 5.19 MB |  |
| ssd r_await (mean) / utilization (mean) | 149.9 µs / 20.07% |  |

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
