#!/usr/bin/env python3
"""Per-block block processing time, all-SSD vs tiered, at W and W2 (same blocks). Writes summary.json and two charts.
usage: tv2_w_vs_w2.py <out dir> <W all-SSD log> <W tiered log> <W2 all-SSD log> <W2 tiered log>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tv2_block_processing import dur_ms, GAS

RX = re.compile(r'\] parallel done +in=(\S+) .*?blk=(\d+) blks=1 .*?txs=(\d+) .*?gas/s=([\d.]+)([KMG]?)')
POS = {'W': 25400000, 'W2': 26130000}


def load(f):
    r = {}
    for line in open(f, errors='replace'):
        m = RX.search(line)
        if m:
            ms = dur_ms(m[1])
            r[int(m[2])] = (ms, float(m[4]) * GAS[m[5]] * ms / 1e3, int(m[3]))
    return r


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def stats(xs):
    return {'mean': round(sum(xs) / len(xs), 1), **{k: round(pct(xs, q), 1) for k, q in (('p50', .5), ('p90', .9), ('p99', .99))}, 'max': round(max(xs), 1)}


def main(out, wssd, wt, w2ssd, w2t):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    res, extra = {}, {}
    for pos, (fs, ft) in (('W', (wssd, wt)), ('W2', (w2ssd, w2t))):
        s, t = load(fs), load(ft)
        bl = sorted(set(s) & set(t))
        extra[pos] = {b: t[b][0] - s[b][0] for b in bl}
        res[pos] = {'blocks': len(bl), 'gas_mgas': stats([s[b][1] for b in bl]), 'txs': stats([s[b][2] for b in bl]),
                    'allssd_ms': stats([s[b][0] for b in bl]), 'tiered_ms': stats([t[b][0] for b in bl]), 'extra_ms': stats(list(extra[pos].values())),
                    'extra_ms_per_1000_blocks': [round(sum(v for b, v in extra[pos].items() if POS[pos] + w * 1000 < b <= POS[pos] + (w + 1) * 1000) /
                                                       max(1, sum(POS[pos] + w * 1000 < b <= POS[pos] + (w + 1) * 1000 for b in bl)), 1) for w in range(10)],
                    'slowest_tiered': [[b, round(t[b][0]), round(s[b][0]), round(s[b][1], 1)] for b in sorted(bl, key=lambda b: -t[b][0])[:5]]}
    json.dump(res, open(os.path.join(out, 'summary.json'), 'w'), indent=1)
    col = {'W': '#1f77b4', 'W2': '#e8a33d'}
    fig, ax = plt.subplots(figsize=(10, 5))
    for pos, e in extra.items():
        xs = sorted(e.values())
        ax.plot(xs, [i / len(xs) for i in range(len(xs))], color=col[pos], label=f'{pos}: mean {res[pos]["extra_ms"]["mean"]} ms, p50 {res[pos]["extra_ms"]["p50"]}, p99 {res[pos]["extra_ms"]["p99"]}, max {res[pos]["extra_ms"]["max"]}')
    ax.set_xscale('symlog', linthresh=10); ax.set_xlabel('extra block processing time per block: tiered 6mo M=64 minus all-SSD, same block (ms)')
    ax.set_ylabel('share of blocks'); ax.grid(alpha=.3); ax.legend(loc='lower right'); ax.set_title('HDD cost per block, W vs W2')
    fig.tight_layout(); fig.savefig(os.path.join(out, 'extra_cdf.png'), dpi=110); plt.close(fig)
    fig, ax = plt.subplots(figsize=(10, 4))
    for i, pos in enumerate(extra):
        ax.bar([w + (i - .5) * .4 for w in range(10)], res[pos]['extra_ms_per_1000_blocks'], .4, color=col[pos], label=pos)
    ax.set_xticks(range(10), [f'{w}k' for w in range(10)]); ax.set_xlabel('blocks into the run'); ax.set_ylabel('mean extra ms per block')
    ax.grid(axis='y', alpha=.3); ax.legend(); ax.set_title('HDD cost per 1,000-block window, W vs W2')
    fig.tight_layout(); fig.savefig(os.path.join(out, 'extra_windows.png'), dpi=110); plt.close(fig)
    print(json.dumps({p: (r['extra_ms'], r['extra_ms_per_1000_blocks']) for p, r in res.items()}))


if __name__ == '__main__':
    main(*sys.argv[1:6])
