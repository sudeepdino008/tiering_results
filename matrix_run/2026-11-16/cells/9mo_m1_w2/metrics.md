# 9mo_m1_w2

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_9mo_m1_w2` |
| commit | `c604cf14` |
| metrics run label | `mx_9mo_m1_w26130000_2026-11-16` |
| blocks | 26,130,000 → 26,139,998 |
| time | 2026-11-19T19:30:31Z → 2026-11-19T21:28:45Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=26140000 --tiering.commitment-hot-merge-steps=1 --tiering.lookback-blocks=1944000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_9mo_m1_w2/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,998 |
| wall time | 1.97 h |
| blocks per second (mean) | 1.41 |
| Mgas/s per block mean / p50 / p5 / p1 | 64.90 / 62.07 / 26.90 / 17.22 |
| Mgas/s wall clock (all-in) | 42.73 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 463.5 ms / 879.5 ms / 1.20 s / 2.18 s |
| exec time per block (exec + commitment) worst | 4.61 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 573.4 ms ± 26.4 ms (n=234) |
| commitment time per block p50 / p90 / p95 / p99 | 179.8 ms / 385.5 ms / 499.1 ms / 1.18 s |
| commitment time per block worst | 3.39 s |
| commitment time per block mean ± 95% CI (30 s windows) | 238.5 ms ± 14.3 ms (n=234) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 140,721 / 153,821 / 285,547 / 376,649 / 878,341 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 207.81 / 438.14 / 891.16 / 947.79 / 993.09 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 27.01 / 48.08 / 91.89 / 97.37 / 653.92 |
| share of probes on HDD | 0.15% |
| share of lookups that reached HDD | 5.55% |
| HDD probe latency p50 / p90 / p95 / p99 | 2.1 µs / 6.5 ms / 14.8 ms / 29.5 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 6.6 µs / 25.0 µs / 1.5 ms |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.20 / 99.90% / 37.95% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 199.55 GB |
| commitment data size on SSD (end) | 1.07 TB |
| commitment index size on SSD (end) | 16.99 GB |
| commitment data + index size, SSD + HDD (end) | 1.29 TB |
| duplicate bytes (max) | 921.70 MB |
| movement lag, straddling_file (blocks: max / end) | 1,558 / 1,283 |
| movement lag, copy_pending (blocks: max / end) | 1,570 / 0 |
| HDD end block / SSD start block (end) | 24,194,709 / 24,194,709 |
| cold merges: count / total seconds / paused seconds | 4.00 / 521.56 s / 122.03 s |
| cold merges: bytes read / written | 11.38 GB / 8.63 GB |
| major page faults per block | 1,910 |
| hdd reads per block / read bytes per block | 33.16 / 643.64 KB |
| hdd r_await (mean) / utilization (mean) | 10.9 ms / 29.57% |
| ssd reads per block / read bytes per block | 1,899 / 9.47 MB |
| ssd r_await (mean) / utilization (mean) | 153.7 µs / 28.50% |

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
