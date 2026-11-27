# W2 with a contiguous cold layout on /sbackup: 6mo M=64, 10,000 blocks, 1 run (stage 17.1)

Same build, blocks and settings as `../2026-11-26` (erigon f32236ec74, blocks 26,130,001..26,140,000, 64 GiB scope, caches dropped,
env `KV_READ_METRICS=false BAL_BATCH_PREFETCH=false`). The only change: the 7 cold commitment files were copied in step order
into a new directory, so that they sit together on /sbackup (0-8192 at 25.6-218.2 GB, the other 6 at 218-304.6 GB of sda1).
In `../2026-11-26` the files were spread over about 8 GB to 1.07 TB of the partition.

| metric | W2 spread layout, M=64 (3 runs, `../2026-11-26/w2_m64_rN`) | W2 contiguous layout, M=64 (`w2c_m64`) | W, M=64 (`../2026-11-25/long_m64`) |
|---|---|---|---|
| newPayload time per block mean / p50 / p99 / worst | 223.8-224.1 / 192.9-193.9 / 823.5-829.1 / 1437-1499 ms | 213.5 / 184.5 / 777.4 / 1337 ms | 207.5 / 151.4 / 1001.4 / 3111 ms |
| Mgas/s per block mean | 152.4-152.7 | 159.2 | 184.2 |
| HDD reads per block | 43.9-44.1 | 44.1 | 48.4 |
| HDD r_await mean | 37.6-37.7 ms | 34.7 ms | 30.3 ms |

Run report: `w2c_m64/metrics.md`; newPayload data: `w2c_m64/newpayload.json`.
