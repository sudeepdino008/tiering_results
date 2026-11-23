# 4mo_m32

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_4mo_m32` |
| commit | `c604cf14` |
| metrics run label | `mx_4mo_m32_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,409,999 |
| time | 2026-11-17T11:31:22Z → 2026-11-17T13:24:06Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=32 --tiering.lookback-blocks=864000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_4mo_m32/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,999 |
| wall time | 1.88 h |
| blocks per second (mean) | 1.48 |
| Mgas/s per block mean / p50 / p5 / p1 | 91.04 / 87.41 / 21.09 / 11.71 |
| Mgas/s wall clock (all-in) | 44.85 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 307.3 ms / 1.06 s / 1.79 s / 3.80 s |
| exec time per block (exec + commitment) worst | 8.03 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 572.4 ms ± 37.9 ms (n=223) |
| commitment time per block p50 / p90 / p95 / p99 | 149.4 ms / 825.2 ms / 1.38 s / 2.86 s |
| commitment time per block worst | 7.77 s |
| commitment time per block mean ± 95% CI (30 s windows) | 397.2 ms ± 35.2 ms (n=223) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 6,753 / 6,248 / 18,450 / 25,873 / 68,999 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 468.97 / 575.34 / 999.37 / 5,473 / 9,095 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 73.63 / 61.44 / 436.91 / 723.33 / 952.46 |
| share of probes on HDD | 6.49% |
| share of lookups that reached HDD | 9.91% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 18.8 ms / 46.0 ms / 138.7 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.8 µs / 6.5 µs / 152.9 µs / 394.1 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.48 / 99.95% / 67.72% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 236.84 GB |
| commitment data size on SSD (end) | 169.58 GB |
| commitment index size on SSD (end) | 8.00 GB |
| commitment data + index size, SSD + HDD (end) | 414.42 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,073 / 10,073 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,535,923 / 24,535,923 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,170 |
| hdd reads per block / read bytes per block | 76.25 / 312.46 KB |
| hdd r_await (mean) / utilization (mean) | 38.2 ms / 60.66% |
| ssd reads per block / read bytes per block | 1,170 / 7.28 MB |
| ssd r_await (mean) / utilization (mean) | 154.8 µs / 23.97% |

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
