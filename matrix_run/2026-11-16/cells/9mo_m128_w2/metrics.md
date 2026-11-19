# 9mo_m128_w2

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_9mo_m128_w2` |
| commit | `c604cf14` |
| metrics run label | `mx_9mo_m128_w26130000_2026-11-16` |
| blocks | 26,130,000 → 26,140,000 |
| time | 2026-11-19T18:15:27Z → 2026-11-19T19:21:05Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=26140000 --tiering.commitment-hot-merge-steps=128 --tiering.lookback-blocks=1944000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_9mo_m128_w2/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 10,000 |
| wall time | 1.09 h |
| blocks per second (mean) | 2.54 |
| Mgas/s per block mean / p50 / p5 | 153.11 / 146.46 / 63.51 |
| Mgas/s wall clock (all-in) | 77.00 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 196.7 ms / 352.4 ms / 439.6 ms / 737.6 ms |
| exec time per block (exec + commitment) worst | 1.49 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 231.2 ms ± 12.2 ms (n=129) |
| commitment time per block p50 / p90 / p95 / p99 | 83.8 ms / 179.3 ms / 222.9 ms / 452.9 ms |
| commitment time per block worst | 1.23 s |
| commitment time per block mean ± 95% CI (30 s windows) | 105.2 ms ± 7.5 ms (n=129) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 3,163 / 5,286 / 9,151 / 9,634 / 13,471 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 146.12 / 331.33 / 867.12 / 934.10 / 987.68 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 27.89 / 48.43 / 92.10 / 97.55 / 673.91 |
| share of probes on HDD | 4.42% |
| share of lookups that reached HDD | 5.55% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.8 µs / 17.8 ms / 32.3 ms / 84.0 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 1.9 µs / 106.3 µs / 204.2 µs / 424.5 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 2.96 / 99.95% / 0.00% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 196.31 GB |
| commitment data size on SSD (end) | 253.76 GB |
| commitment index size on SSD (end) | 8.84 GB |
| commitment data + index size, SSD + HDD (end) | 458.91 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,819 / 10,819 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 24,185,177 / 24,185,177 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 860.99 |
| hdd reads per block / read bytes per block | 28.87 / 118.32 KB |
| hdd r_await (mean) / utilization (mean) | 24.5 ms / 38.94% |
| ssd reads per block / read bytes per block | 841.71 / 4.26 MB |
| ssd r_await (mean) / utilization (mean) | 140.8 µs / 28.38% |

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
