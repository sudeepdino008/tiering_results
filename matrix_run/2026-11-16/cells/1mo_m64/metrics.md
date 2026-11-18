# 1mo_m64

| | |
|---|---|
| kind | demotion |
| datadir | `/erigon-data/tv2_mx_1mo_m64` |
| commit | `c604cf14` |
| metrics run label | `mx_1mo_m64_w25400000_2026-11-16` |
| blocks | 25,400,000 → 25,409,995 |
| time | 2026-11-18T10:36:30Z → 2026-11-18T13:59:07Z |

Flags:

```
KV_READ_METRICS=true --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=25410000 --tiering.commitment-hot-merge-steps=64 --tiering.lookback-blocks=216000 --tiering.cold-dir=/backup/erigon-hdd/tv2_mx_1mo_m64/domain --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=6080 --tiering.cold-io-max-mbps=50 --pfb.sync.mode.chaintip
```

## Summary

| Metric | Value |
|---|---|
| blocks executed | 9,995 |
| wall time | 3.38 h |
| blocks per second (mean) | 0.82 |
| Mgas/s per block mean / p50 / p5 | 48.38 / 46.28 / 9.29 |
| Mgas/s wall clock (all-in) | 24.95 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 591.9 ms / 2.40 s / 4.25 s / 8.85 s |
| exec time per block (exec + commitment) worst | 21.08 s |
| exec time per block (exec + commitment) mean ± 95% CI (30 s windows) | 1.33 s ± 84.2 ms (n=404) |
| commitment time per block p50 / p90 / p95 / p99 | 317.7 ms / 2.06 s / 3.82 s / 8.36 s |
| commitment time per block worst | 20.81 s |
| commitment time per block mean ± 95% CI (30 s windows) | 1.04 s ± 82.8 ms (n=404) |
| ssd probes per block mean / p50 / p90 / p95 / p99 | 3,795 / 5,483 / 9,665 / 15,507 / 27,790 |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 1,064 / 691.38 / 6,385 / 8,254 / 9,750 |
| hdd slow probes per block mean / p50 / p90 / p95 / p99 | 175.96 / 88.17 / 827.90 / 939.82 / 6,106 |
| share of probes on HDD | 21.91% |
| share of lookups that reached HDD | 20.14% |
| HDD probe latency p50 / p90 / p95 / p99 | 1.9 µs / 21.4 ms / 55.3 ms / 189.8 ms |
| SSD probe latency p50 / p90 / p95 / p99 (sampled) | 2.0 µs / 9.5 µs / 177.5 µs / 396.1 µs |
| HDD probes per lookup that reached HDD: mean / share > 1 / share > 4 | 4.99 / 96.28% / 59.41% |
| existence-filter false positives (HDD / SSD) | 0 / 0 |
| commitment data size on HDD (end) | 296.13 GB |
| commitment data size on SSD (end) | 36.22 GB |
| commitment index size on SSD (end) | 7.03 GB |
| commitment data + index size, SSD + HDD (end) | 339.38 GB |
| duplicate bytes (max) | 0 B |
| movement lag, straddling_file (blocks: max / end) | 10,177 / 10,177 |
| movement lag, copy_pending (blocks: max / end) | 0 / 0 |
| HDD end block / SSD start block (end) | 25,183,816 / 25,183,816 |
| cold merges: count / total seconds / paused seconds | 0 / 0.0 µs / 0.0 µs |
| cold merges: bytes read / written | 0 B / 0 B |
| major page faults per block | 1,008 |
| hdd reads per block / read bytes per block | 186.82 / 765.43 KB |
| hdd r_await (mean) / utilization (mean) | 46.3 ms / 79.20% |
| ssd reads per block / read bytes per block | 978.35 / 5.89 MB |
| ssd r_await (mean) / utilization (mean) | 161.9 µs / 13.47% |

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
