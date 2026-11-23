# 1mo_m4

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_1mo_m4` |
| commit | `c604cf14` |
| metrics run label | `mx_1mo_m4_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,410,000 |
| time | 2026-11-18T01:57:17Z → 2026-11-18T05:19:12Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=4 --tiering.lookback-blocks=216000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_1mo_m4/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 3.37 h |
| blocks per second (mean) | 0.83 |
| Mgas/s per block mean / p50 / p5 / p1 | 48.63 / 46.37 / 9.36 / 5.40 |
| Mgas/s wall clock (all-in) | 25.04 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 589.5 ms / 2.38 s / 4.24 s / 8.85 s |
| exec time per block (exec + commitment) worst | 21.25 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 1.33 s ± 86.8 ms (n=401) |
| commitment time per block p50 / p90 / p95 / p99 | 314.5 ms / 2.05 s / 3.81 s / 8.32 s |
| commitment time per block worst | 20.97 s |
| commitment time per block mean ± 95% CI (30 s windows) | 1.05 s ± 85.6 ms (n=401) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 14,873 / 9,133 / 36,939 / 70,952 / 98,163 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 1,201 / 713.06 / 6,759 / 8,459 / 9,820 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 176.77 / 88.59 / 829.87 / 941.07 / 6,170 |
| share of probes on HDD | 7.47% |
| share of lookups that reached HDD | 20.20% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 17.6 ms / 47.2 ms / 179.0 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.7 µs / 2.5 µs / 6.5 µs / 244.3 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 5.61 / 98.29% / 71.64% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 297.75 GB |
| commitment data size on SSD (end) | 80.00 GB |
| commitment index size on SSD (end) | 7.41 GB |
| commitment data + index size, SSD + HDD (end) | 385.16 GB |
| duplicate bytes (max) | 1.58 GB |
| movement lag, straddling_file (blocks: max / end) | 5,253 / 5,253 |
| movement lag, copy_pending (blocks: max / end) | 4,927 / 0 |
| HDD end block / SSD start block (end) | 25,188,743 / 25,188,743 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,085 |
| hdd reads per block / read bytes per block | 187.18 / 766.98 KB |
| hdd r_await (mean) / utilization (mean) | 45.7 ms / 78.90% |
| ssd reads per block / read bytes per block | 1,057 / 5.76 MB |
| ssd r_await (mean) / utilization (mean) | 153.9 µs / 14.33% |

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
