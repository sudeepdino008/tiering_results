#!/usr/bin/env python3
"""Per-block block processing time from an erigon chaintip log: the 'parallel done in=' span of each one-block ExecV3 cycle
(warmup, execution, commitment fold and root; no flush/commit). Same span as exec_block_seconds, without histogram buckets.
usage: tv2_block_processing.py <run.log> <out dir>   |   --selftest      writes <out dir>/block_processing.json"""
import json, os, re, sys

DONE = re.compile(r'\] parallel done +in=(\S+) .*?blk=(\d+) blks=1 .*?gas/s=([\d.]+)([KMG]?)')
UNIT_MS = {'ns': 1e-6, 'µs': 1e-3, 'us': 1e-3, 'ms': 1, 's': 1e3, 'm': 6e4, 'h': 3.6e6}
GAS = {'': 1e-6, 'K': 1e-3, 'M': 1, 'G': 1e3}


def dur_ms(s):
    return sum(float(v) * UNIT_MS[u] for v, u in re.findall(r'([\d.]+)(ns|µs|us|ms|s|m|h)', s))


def parse(lines):
    rows = {}
    for line in lines:
        m = DONE.search(line)
        if m:
            rows[int(m[2])] = (dur_ms(m[1]), float(m[3]) * GAS[m[4]])
    return rows


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def summary(rows):
    ms = [v[0] for v in rows.values()]
    mg = [v[1] for v in rows.values()]
    return {'blocks': len(rows), 'bpt_mean_ms': round(sum(ms) / len(ms), 1), 'bpt_p50_ms': round(pct(ms, .5), 1), 'bpt_p99_ms': round(pct(ms, .99), 1),
            'bpt_worst_ms': round(max(ms), 1), 'bpt_worst_block': max(rows, key=lambda b: rows[b][0]), 'bpt_mgas_s_mean': round(sum(mg) / len(mg), 2),
            'bpt_mgas_s_p50': round(pct(mg, .5), 2)}


def selftest():
    log = ['[INFO] [11-26|11:42:04.084] [4/6 Execution] parallel done            in=482.030609ms buf=569.2KB/512.0MB blk=26130001 blks=1 blk/s=2 txs=338 tx/s=701 gas/s=124.45M stepsInDB=0.41',
           '[INFO] [11-26|11:42:05.195] [4/6 Execution] parallel done            in=1.5s buf=532.4KB/512.0MB blk=26130002 blks=1 blk/s=2 txs=338 tx/s=942 gas/s=900K stepsInDB=0.41',
           '[INFO] [11-26|11:42:06.099] [4/6 Execution] parallel done            in=72ms buf=1KB blk=26130003 blks=2 gas/s=1M']
    r = parse(log)
    assert r == {26130001: (482.030609, 124.45), 26130002: (1500.0, 0.9)}, r
    s = summary(r)
    assert s['bpt_worst_ms'] == 1500 and s['bpt_worst_block'] == 26130002 and s['bpt_p50_ms'] == 1500 and s['blocks'] == 2, s
    print('selftest ok')


if __name__ == '__main__':
    if sys.argv[1:] == ['--selftest']:
        selftest()
    else:
        with open(sys.argv[1], errors='replace') as f:
            s = summary(parse(f))
        json.dump(s, open(os.path.join(sys.argv[2], 'block_processing.json'), 'w'), indent=1)
        print(sys.argv[2], s)
