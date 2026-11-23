# 4mo_m4

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_4mo_m4` |
| commit | `c604cf14` |
| metrics run label | `mx_4mo_m4_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,409,993 |
| time | 2026-11-17T08:42:23Z → 2026-11-17T10:37:49Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=4 --tiering.lookback-blocks=864000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_4mo_m4/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,993 |
| wall time | 1.92 h |
| blocks per second (mean) | 1.44 |
| Mgas/s per block mean / p50 / p5 / p1 | 87.04 / 83.97 / 20.41 / 11.58 |
| Mgas/s wall clock (all-in) | 43.80 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 322.6 ms / 1.08 s / 1.83 s / 3.85 s |
| exec time per block (exec + commitment) worst | 8.50 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 586.4 ms ± 39.1 ms (n=228) |
| commitment time per block p50 / p90 / p95 / p99 | 157.3 ms / 838.6 ms / 1.42 s / 3.12 s |
| commitment time per block worst | 8.24 s |
| commitment time per block mean ± 95% CI (30 s windows) | 406.1 ms ± 37.1 ms (n=228) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 34,321 / 22,853 / 90,392 / 164,009 / 282,269 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 492.15 / 579.89 / 1,467 / 5,734 / 9,147 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 73.59 / 61.35 / 431.53 / 721.27 / 953.07 |
| share of probes on HDD | 1.41% |
| share of lookups that reached HDD | 9.94% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 16.6 ms / 42.7 ms / 127.2 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.7 µs / 2.5 µs / 7.4 µs / 353.1 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.69 / 99.78% / 71.58% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 239.30 GB |
| commitment data size on SSD (end) | 326.64 GB |
| commitment index size on SSD (end) | 9.25 GB |
| commitment data + index size, SSD + HDD (end) | 575.19 GB |
| duplicate bytes (max) | 1.68 GB |
| movement lag, straddling_file (blocks: max / end) | 5,205 / 794 |
| movement lag, copy_pending (blocks: max / end) | 5,206 / 0 |
| HDD end block / SSD start block (end) | 24,545,181 / 24,545,181 |
| cold merges: count / total seconds / paused seconds | 2.00 / 455.19 s / 234.13 s |
| cold merges: bytes read / written | 6.11 GB / 5.07 GB |
| major page faults per block | 1,376 |
| hdd reads per block / read bytes per block | 78.64 / 573.39 KB |
| hdd r_await (mean) / utilization (mean) | 36.1 ms / 60.80% |
| ssd reads per block / read bytes per block | 1,367 / 6.83 MB |
| ssd r_await (mean) / utilization (mean) | 147.1 µs / 25.45% |

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
