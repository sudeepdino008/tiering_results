# tiering_results

Erigon state-tiering v2 runs. One folder per run: `<run>/metrics.md`, graphs in `<run>/images/`.

Run name: `<kind>_<tiering>_<commitment files>_<lookback>_<variant>_<YYYY-MM-DD>-<n>`, e.g.
`baseline_allssd_merged_6mo_w25400000_2026-10-23-2` (kind `baseline`|`demote`; tiering `allssd`|`hdd0`|`tiered`;
commitment files `1step`|`merged`). The run name is also the `run` label in the metrics store.

### Note about the tiering runs:

- the runs start from `W = 25400000` (June 26, 2026)
- all runs execute 10k blocks (in today's erigon it takes about 40 minutes) -- this has shown to stabilize the perf numbers while proving enough room for demotions AND merge of HDD files to take place.
- 10k blocks should produce 6 commitment files, and we should see demotions of approximately as many files in that 40 minute period. We should also see merges happening in HDD.

## Machine

| | |
|---|---|
| CPU | Intel Xeon W-2145 @ 3.70 GHz (max 4.5 GHz), 1 socket, 8 cores, 16 threads |
| RAM | 125 GiB; swap 4 GiB (partition on the NVMe) |
| SSD (hot tier) | Toshiba KXD51RUE3T84, 3.84 TB NVMe, ext4 `rw,relatime`, scheduler `none`, read-ahead 128 KB, mounted at `/` (datadirs in `/erigon-data`) |
| HDD (cold tier) | HGST HUS726060AL, 6 TB SATA 7200 rpm, ext4 `rw,relatime`, scheduler `mq-deadline`, read-ahead 128 KB, mounted at `/backup` |
| OS | Ubuntu 24.04.3 LTS, kernel 6.8.0-90-generic |

### Kernel settings (sysctl) for the runs

```
vm.dirty_ratio = 20
vm.dirty_background_ratio = 10
vm.dirty_expire_centisecs = 3000
vm.dirty_writeback_centisecs = 500
vm.swappiness = 60
vm.vfs_cache_pressure = 100
vm.overcommit_memory = 1
vm.max_map_count = 16777216
vm.min_free_kbytes = 67584
kernel.numa_balancing = 0
```

Before each run, the run script drops the page cache:

```
sync; sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'
```

To check the values on the machine:

```
sysctl vm.dirty_ratio vm.dirty_background_ratio vm.dirty_expire_centisecs vm.dirty_writeback_centisecs \
  vm.swappiness vm.vfs_cache_pressure vm.overcommit_memory vm.max_map_count vm.min_free_kbytes kernel.numa_balancing
cat /sys/block/{nvme0n1,sda}/queue/{scheduler,read_ahead_kb}
```
