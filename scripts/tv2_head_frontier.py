#!/usr/bin/env python3
"""Frontier charts (SSD commitment GB vs Mgas/s, commitment p50 / p99 / worst) for 10,000-block runs on one build.
usage: tv2_head_frontier.py <out dir> <baseline report dir> <L>:<M>:<report dir> [...]   |   --selftest"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tv2_matrix_report as R

ROW = r'\| {} \| ([^|]+) \|'


def ms(v):
    n, u = re.match(r'([\d.,]+) ?(µs|ms|s)', v.strip()).groups()
    return round(float(n.replace(',', '')) * {'µs': 1e-3, 'ms': 1, 's': 1e3}[u], 1)


def read(d):
    t = open(os.path.join(d, 'metrics.md')).read()
    g = lambda k: re.search(ROW.format(re.escape(k)), t)[1]
    commit = g('commitment time per block p50 / p90 / p95 / p99').split(' / ')
    ssd = g('commitment data size on SSD (end)').split()
    return {'mgas_s_per_block': float(g('Mgas/s per block mean / p50 / p5 / p1').split(' / ')[0].replace(',', '')),
            'commit_p50_ms': ms(commit[0]), 'commit_p95_ms': ms(commit[2]), 'commit_p99_ms': ms(commit[3]),
            'commit_worst_ms': ms(g('commitment time per block worst')),
            'ssd_commit_gb': float(ssd[0]) * {'GB': 1, 'TB': 1e3, 'MB': 1e-3}[ssd[1]], 'rc': 0, 'W': R.W1}


def main(out, base, cells):
    b = read(base)
    R.BASELINE.update(b, name=os.path.basename(base))
    R.BASELINE['mgas_s_per_block'] = round(b['mgas_s_per_block'])
    rows = {}
    for c in cells:
        L, M, d = c.split(':', 2)
        rows[(L, int(M))] = dict(read(d), L=L, M=int(M))
    R.LS = R.GRID_LS = sorted({L for L, _ in rows})
    R.MS = sorted({M for _, M in rows})
    style = R.style
    R.style = lambda ax, *a: (style(ax, *a), ax.set_ylim(bottom=0))
    os.makedirs(out, exist_ok=True)
    R.charts(out, rows, None, len(rows))
    for f in ('trends', 'progress'):
        for ext in ('png', 'svg'):
            os.remove(os.path.join(out, f'{f}.{ext}'))
    json.dump({'baseline': R.BASELINE, 'cells': {f'{L}/{M}': s for (L, M), s in rows.items()}}, open(os.path.join(out, 'frontier.json'), 'w'), indent=1)


def selftest():
    assert ms('1.01 s') == 1010 and ms('235.6 ms') == 235.6 and ms('0.7 µs') == 0.0
    print('selftest ok')


if __name__ == '__main__':
    selftest() if sys.argv[1:] == ['--selftest'] else main(sys.argv[1], sys.argv[2], sys.argv[3:])
