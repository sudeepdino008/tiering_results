#!/usr/bin/env python3
"""Stage 17.1: one markdown table over the short prefetch runs. usage: tv2_pf_compare.py <results day dir> <tag> [<tag> ...]"""
import json, os, sys

ROWS = ['Mgas/s per block mean / p50 / p5 / p1', 'exec time per block (exec + commitment) p50 / p90 / p95 / p99',
        'commitment time per block p50 / p90 / p95 / p99', 'commitment time per block worst', 'exec time per block (exec + commitment) worst', 'hdd probes per block mean / p50 / p90 / p95 / p99',
        'HDD probe latency p50 / p90 / p95 / p99', 'major page faults per block', 'hdd reads per block / read bytes per block',
        'hdd r_await (mean) / utilization (mean)', 'ssd reads per block / read bytes per block', 'blocks executed']


def metrics(d):
    out = {}
    for line in open(os.path.join(d, 'metrics.md')):
        p = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(p) == 2:
            out.setdefault(p[0], p[1])
    return out


def pf(d):
    f = os.path.join(d, 'prefetch_summary.json')
    if not os.path.exists(f):
        return {}
    s = json.load(open(f))
    q = lambda k: f"{s[k]['p50']:.1f} / {s[k]['p95']:.1f}"
    sh = s['elapsed_share_of_exec']
    return {
        'prefetch blocks logged': str(s['blocks']),
        'prefetch elapsed ms p50 / p95': q('elapsed_ms'),
        'trie / sample / state ms p50': ' / '.join(f"{s[k]['p50']:.1f}" for k in ('trie_ms', 'sample_ms', 'state_ms')),
        'perKey ms p50 / p95': q('perKey_ms'),
        'trie warmuper ms p50 / p95': q('trieWarm_ms') if 'trieWarm_ms' in s else '—',
        'elapsed / exec p50 / p95; blocks elapsed > exec': f"{sh['p50']:.2f} / {sh['p95']:.2f}; {sh['blocks_elapsed_gt_exec']:.0%}",
        'cancelled blocks': str(s['cancelled_blocks']),
        'io_uring read ms per block p50 / p95': q('all_readMs'),
        'mincore calls / ms per block p50': f"{s['all_mincores']['p50']:.0f} / {s['all_mincoreMs']['p50']:.1f}",
        'mincore calls vs 16 / 64 / 256-page windows (per call) / 64-page windows (per block), per block p50':
            f"{s['all_mincores']['p50']:.0f} vs {s['all_win16']['p50']:.0f} / {s['all_win64']['p50']:.0f} / {s['all_win256']['p50']:.0f} / {s['all_blockWin64']['p50']:.0f}" if 'all_win64' in s else '—',
        'rest of block (block - exec - commit) ms p50 / p95': f"{s['rest_ms']['p50']:.0f} / {s['rest_ms']['p95']:.0f}" if 'rest_ms' in s else '—',
        'probe ms per block p50': f"{s['all_probeMs']['p50']:.1f}",
        'pages per block p50 / p95': f"{s['all_pages']['p50']:.0f} / {s['all_pages']['p95']:.0f}",
        'waves per call mean / max': f"{s['waves_per_call']['mean'] or 0:.2f} / {s['waves_per_call']['max'] or 0:.0f}",
        'incomplete calls / share of blocks': f"{s['incomplete']['calls']:.0f} / {s['incomplete']['block_share']:.1%}",
    }


day, tags = sys.argv[1], sys.argv[2:]
cols = {t: {**metrics(os.path.join(day, t)), **pf(os.path.join(day, t)),
            'run checks': open(os.path.join(day, t, 'summary.txt')).read().split(' last block')[0].strip()} for t in tags}
keys = ROWS + [k for k in pf(os.path.join(day, tags[-1])) if k] + ['run checks']
print('| metric | ' + ' | '.join(tags) + ' |')
print('|---|' + '---|' * len(tags))
for k in keys:
    print(f'| {k} | ' + ' | '.join(cols[t].get(k, '—') for t in tags) + ' |')
