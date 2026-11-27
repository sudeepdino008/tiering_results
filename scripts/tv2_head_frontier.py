#!/usr/bin/env python3
"""Frontier charts (SSD commitment GB vs Mgas/s and newPayload time per block p50 / p99 / worst) for 10,000-block runs on one build.
newPayload time = the 'parallel done in=' span from <report dir>/newpayload.json (tv2_newpayload.py).
usage: [AT=W2] tv2_head_frontier.py <out dir> <baseline report dirs> <L>:<M>:<report dirs> [...]   |   --selftest
<report dirs> is one dir or a comma-separated list of repeats; charts plot the mean with a min-max bar, frontier.json also keeps min and max."""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tv2_matrix_report as R

ROW = r'\| {} \| ([^|]+) \|'
NP = ('np_p50_ms', 'np_p99_ms', 'np_worst_ms')
R.FRONTIERS = [R.FRONTIERS[0], ('np_p50', 'np_p50_ms', 'newPayload time p50 ms per block (lower is better)', False),
               ('np_p99', 'np_p99_ms', 'newPayload time p99 ms per block (lower is better)', False)]
R.WORST = ('np_worst', 'np_worst_ms', 'newPayload time worst ms per block (lower is better)', False)
R.BASE_UNIT.update(np_p50_ms='ms p50', np_p99_ms='ms p99', np_worst_ms='ms worst')


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
            'ssd_commit_gb': float(ssd[0]) * {'GB': 1, 'TB': 1e3, 'MB': 1e-3}[ssd[1]], 'rc': 0, 'W': R.W1,
            **{k: v for k, v in json.load(open(os.path.join(d, 'newpayload.json'))).items() if k in NP}}


def mean(dirs):
    rs = [read(d) for d in dirs.split(',')]
    out = {k: round(sum(r[k] for r in rs) / len(rs), 2) for k in rs[0]}
    for k in ('mgas_s_per_block',) + NP:
        out[k + '_min'], out[k + '_max'] = min(r[k] for r in rs), max(r[k] for r in rs)
    return dict(out, repeats=len(rs))


def main(out, base, cells):
    b = mean(base)
    R.BASELINE.update(b, name=os.path.basename(base.split(',')[0]))
    R.BASELINE['mgas_s_per_block'] = round(b['mgas_s_per_block'])
    rows = {}
    for c in cells:
        L, M, d = c.split(':', 2)
        rows[(L, int(M))] = dict(mean(d), L=L, M=int(M))
    R.LS = R.GRID_LS = sorted({L for L, _ in rows})
    R.MS = sorted({M for _, M in rows})
    R.BASE_AT, R.W2_SSD_GB = os.environ.get('AT', 'W'), None
    keys = {f[2]: f[1] for f in R.FRONTIERS + [R.WORST]}
    style = R.style

    def styled(ax, xlabel, ylabel):
        k = keys.get(ylabel)
        for s in list(rows.values()) + [R.BASELINE] if k else []:
            if k + '_min' in s:
                ax.vlines(s['ssd_commit_gb'], s[k + '_min'], s[k + '_max'], color=R.INK2, lw=1, zorder=2)
        style(ax, xlabel, ylabel)
        ax.set_ylim(0, ax.get_ylim()[1] * 1.12)
    R.style = styled
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
