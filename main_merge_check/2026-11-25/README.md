# Main merge check: long run, BAL batch prefetch off (stage 17.1)

10,000 chaintip blocks 25,400,001..25,410,000 from W = 25,400,000, tiered 6mo, M = 64 (`--tiering.commitment-hot-merge-steps=64`),
cold files on `/sbackup`, demotion on, offline BALs, state cache on, `--tiering.cold-io-max-mbps=50`, erigon f32236ec74 (main merge),
64 GiB memory scope (page cache included), page caches dropped before the start.
Env: `KV_READ_METRICS=false BAL_BATCH_PREFETCH=false WARMBAL_STATS=true` (io_uring BAL batch prefetch off; trie warmuper and per-key BAL warmup on).

| metric | long_off_nokv |
|---|---|
| Mgas/s per block mean / p50 / p5 / p1 | 184.16 / 176.93 / 58.85 / 36.35 |
| exec time per block (exec + commitment) p50 / p90 / p95 / p99 | 152.3 ms / 391.7 ms / 608.1 ms / 1.01 s |
| commitment time per block p50 / p90 / p95 / p99 | 18.7 ms / 36.9 ms / 44.3 ms / 54.2 ms |
| hdd probes per block mean / p50 / p90 / p95 / p99 | 311.24 / 479.59 / 950.55 / 2,241 / 8,448 |
| HDD probe latency p50 / p90 / p95 / p99 | 0.7 µs / 17.5 ms / 38.9 ms / 94.3 ms |
| major page faults per block | 1,114 |
| hdd reads per block / read bytes per block | 48.42 / 198.38 KB |
| hdd r_await (mean) / utilization (mean) | 30.3 ms / 35.49% |
| ssd reads per block / read bytes per block | 1,117 / 6.10 MB |
| blocks executed | 9,983 |
| prefetch blocks logged | 10000 |
| prefetch elapsed ms p50 / p95 | 107.7 / 465.7 |
| trie / sample / state ms p50 | 0.0 / 0.0 / 0.0 |
| perKey ms p50 / p95 | 4.9 / 19.0 |
| trie warmuper ms p50 / p95 | 106.9 / 464.4 |
| elapsed / exec p50 / p95; blocks elapsed > exec | 1.11 / 2.18; 65% |
| cancelled blocks | 5912 |
| io_uring read ms per block p50 / p95 | 0.0 / 0.0 |
| mincore calls / ms per block p50 | 0 / 0.0 |
| mincore calls vs 16 / 64 / 256-page windows (per call) / 64-page windows (per block), per block p50 | 0 vs 0 / 0 / 0 / 0 |
| rest of block (block - exec - commit) ms p50 / p95 | 29 / 124 |
| probe ms per block p50 | 0.0 |
| pages per block p50 / p95 | 0 / 0 |
| waves per call mean / max | 0.00 / 0 |
| incomplete calls / share of blocks | 0 / 0.0% |
| run checks | rc=0 root_errors=0 oom_kill=0 memmax64g=1 precheck_after=FAIL io_uring_disabled_lines=0 stats_lines=10000 files_changed=0 files_removed=44 |
