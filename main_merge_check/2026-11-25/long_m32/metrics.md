# long_m32

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_pf_6mo_m32_long_m32_nokv` |
| commit | `f32236ec` |
| metrics run label | `pf_6mo_m32_long_m32_nokv_10000b_w25400000_2026-11-25` |
| blocks | 25,400,000 → 25,409,979 |
| time | 2026-11-25T16:41:52Z → 2026-11-25T17:35:47Z |

Flags:

```
KV_READ_METRICS=false --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=32 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/sbackup/tv2_pf_6mo_m32_long_m32_nokv/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50  --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,979 |
| wall time | 0.90 h |
| blocks per second (mean) | 3.08 |
| Mgas/s per block mean / p50 / p5 / p1 | 184.67 / 177.36 / 60.14 / 36.23 |
| Mgas/s wall clock (all-in) | 93.81 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 152.1 ms / 392.7 ms / 608.8 ms / 1.01 s |
| exec time per block (exec + commitment) worst | 3.11 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 222.5 ms ± 15.0 ms (n=105) |
| commitment time per block p50 / p90 / p95 / p99 | 18.6 ms / 36.6 ms / 44.2 ms / 55.1 ms |
| commitment time per block worst | 179.2 ms |
| commitment time per block mean ± 95% CI (30 s windows) | 19.4 ms ± 387.9 µs (n=105) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 7,890 / 6,472 / 21,706 / 28,403 / 82,028 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 311.51 / 478.99 / 950.62 / 2,258 / 8,452 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 51.55 / 57.26 / 215.93 / 609.15 / 923.72 |
| share of probes on HDD | 3.80% |
| share of lookups that reached HDD | 7.67% |
| HDD probe latency p50 / p90 / p95 / p99 | 0.7 µs / 17.5 ms / 38.9 ms / 94.2 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 0.7 µs / 3.7 µs / 146.9 µs / 440.6 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 3.98 / 99.65% / 0.00% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 185.62 GB |
| commitment data size on SSD (end) | 269.64 GB |
| commitment index size on SSD (end) | 8.60 GB |
| commitment data + index size, SSD + HDD (end) | 463.86 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,331 / 10,331 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,103,642 / 24,103,642 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,152 |
| hdd reads per block / read bytes per block | 48.50 / 198.70 KB |
| hdd r_await (mean) / utilization (mean) | 30.3 ms / 35.38% |
| ssd reads per block / read bytes per block | 1,155 / 6.20 MB |
| ssd r_await (mean) / utilization (mean) | 197.6 µs / 33.99% |

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
