# w2s_ctl

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_pf_6mo_m32_w2_w2s_ctl` |
| commit | `f32236ec` |
| metrics run label | `pf_6mo_m32_w2_w2s_ctl_2000b_w26130000_2026-11-26` |
| blocks | 26,130,000 → 26,132,000 |
| time | 2026-11-26T22:57:35Z → 2026-11-26T23:08:08Z |

Flags:

```
KV_READ_METRICS=false --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=26132000 --tiering.commitment-hot-merge-steps=32 --tiering.lookback-blocks=1296000 --tiering.cold-dir=/sbackup/tv2_pf_6mo_m32_w2_w2s_ctl/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50  --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 2,000 |
| wall time | 0.18 h |
| blocks per second (mean) | 3.16 |
| Mgas/s per block mean / p50 / p5 / p1 | 189.55 / 185.29 / 76.81 / 50 |
| Mgas/s wall clock (all-in) | 96.25 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 153.5 ms / 280.3 ms / 361.1 ms / 716.7 ms |
| exec time per block (exec + commitment) worst | 1.32 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 175.9 ms ± 8.1 ms (n=19) |
| commitment time per block p50 / p90 / p95 / p99 | 17.8 ms / 30.5 ms / 41.0 ms / 49.5 ms |
| commitment time per block worst | 107.4 ms |
| commitment time per block mean ± 95% CI (30 s windows) | 17.9 ms ± 548.8 µs (n=19) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 3,576 / 5,414 / 9,334 / 9,824 / 24,194 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 308.08 / 518.20 / 925.21 / 976.09 / 6,604 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 33.15 / 52.84 / 93.06 / 98.09 / 709.68 |
| share of probes on HDD | 7.93% |
| share of lookups that reached HDD | 6.48% |
| HDD probe latency p50 / p90 / p95 / p99 | 0.7 µs / 5.6 ms / 26.9 ms / 85.6 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 0.8 µs / 132.9 µs / 232.6 µs / 489.5 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 6.49 / 99.92% / 95.74% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 261.55 GB |
| commitment data size on SSD (end) | 255.40 GB |
| commitment index size on SSD (end) | 9.69 GB |
| commitment data + index size, SSD + HDD (end) | 526.63 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 2,916 / 2,916 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,833,066 / 24,833,066 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,541 |
| hdd reads per block / read bytes per block | 29.44 / 121.58 KB |
| hdd r_await (mean) / utilization (mean) | 33.3 ms / 31.07% |
| ssd reads per block / read bytes per block | 1,586 / 11.75 MB |
| ssd r_await (mean) / utilization (mean) | 153.7 µs / 35.13% |

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
