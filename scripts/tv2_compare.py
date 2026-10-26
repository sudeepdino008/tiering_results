#!/erigon-data/tv2_scripts/.venv/bin/python
"""Compare two tiering v2 runs: summary table side by side with B/A ratios, and each dashboard panel with both runs
on one graph (x = execution block, so runs over the same blocks line up).
usage: tv2_compare.py <run A> <run B> [--label-a A] [--label-b B] [--name NAME] [--out DIR] [--push] [--no-png]"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from tv2_report import M, PANEL_NOTES, fmt, iso, prom, push, run_range, summary
import json

STEP = 30
RATE = '2m'
OMIT = {'commitment_index_size'}
LEGEND = dict(fontsize=7, ncol=2, loc='upper center', bbox_to_anchor=(0.5, -0.2), frameon=False)
YLABEL = {'exec_height': 'block', 'blk_s': 'blocks/s', 'mgas_s': 'Mgas/s', 'probes_per_block': 'probes per block',
          'hdd_probe_share': 'share', 'slow_probes': 'probes/s', 'lag_blocks': 'blocks', 'tier_edges': 'block',
          'demotions': 'demotions (count)', 'cold_merge': 'share / steps / count', 'major_faults': 'faults/s',
          'disk_reads': 'reads/s'}


def ratio(a, b):
    if a is None or b is None or a == 0:
        return '—'
    return f'{b / a:.2f}×'


def legend(fmt_, labels):
    return re.sub(r'\{\{(\w+)\}\}', lambda m: labels.get(m.group(1), ''), fmt_ or '')


def panel_series(expr, run, t0, t1):
    q = expr.replace('$run', run).replace('$__rate_interval', RATE)
    return prom('query_range', query=q, start=t0, end=t1, step=STEP)


def height_at(run, t0, t1):
    res = prom('query_range', query=f'max(sync{{stage="execution",run="{run}"}})', start=t0, end=t1, step=STEP)
    return {float(t): float(v) for t, v in res[0]['values']} if res else {}


def tick(v, unit):
    if v == 0:
        return '0'
    if unit == '' and abs(v) >= 1e3:
        return f'{v / 1e3:.0f}k'
    return re.sub(r'\.0+(?=\D|$)', '', fmt(v, unit))


def plot_panel(p, runs, path):
    by_block = p['description'] != 'exec_height'
    fig, ax = plt.subplots(figsize=(10, 4))
    rax = None
    styles = ['-', '--', ':', '-.']
    peaks, drawn = [], 0
    for color, (label, run, t0, t1, height) in zip(('tab:blue', 'tab:orange'), runs):
        i, peak = 0, 0.0
        for t in p.get('targets', []):
            for s in panel_series(t['expr'], run, t0, t1):
                pts = [(height.get(float(ts)) if by_block else (float(ts) - t0) / 60, float(v)) for ts, v in s['values']]
                pts = [(x, y) for x, y in pts if x is not None and y == y and abs(y) != float('inf')]
                if not pts:
                    continue
                xs, ys = zip(*pts)
                name = legend(t.get('legendFormat'), s['metric']) or t['expr'][:30]
                if not any(ys):
                    ax.plot([], [], ' ', label=f'{label}: {name} (all 0, not drawn)')
                    continue
                if '(B/s)' in name:
                    rax = rax or ax.twinx()
                    rax.plot(xs, ys, styles[i % len(styles)], color=color, lw=1, label=f'{label}: {name} (right axis)')
                    i += 1
                    continue
                peak = max(peak, max(abs(y) for y in ys))
                ax.plot(xs, ys, styles[i % len(styles)], color=color, lw=1, label=f'{label}: {name}')
                i += 1
        peaks.append(peak)
        drawn += i
    nonzero = [x for x in peaks if x > 0]
    if nonzero and max(nonzero) > 20 * min(nonzero):
        ax.set_yscale('symlog', linthresh=min(nonzero) / 10)
    elif drawn and 0 < ax.get_ylim()[0] < ax.get_ylim()[1] / 2:
        ax.set_ylim(bottom=0)
    unit = p.get('fieldConfig', {}).get('defaults', {}).get('unit', '')
    tick_unit, suffix = {'bytes': ('B', ''), 'Bps': ('B', '/s'), 's': ('s', ''), 'percentunit': ('%', '')}.get(unit, ('', ''))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: tick(v, tick_unit) + suffix))
    if by_block:
        ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: tick(v, '')))
    ax.set_title(p['title'])
    ax.set_xlabel('execution block' if by_block else 'minutes since run start')
    ax.set_ylabel(YLABEL.get(p['description'], ''))
    if rax:
        rax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: '0' if v == 0 else tick(v, 'B') + '/s'))
        rax.set_ylim(bottom=0)
        h, l = ax.get_legend_handles_labels()
        rh, rl = rax.get_legend_handles_labels()
        ax.legend(h + rh, l + rl, **LEGEND)
    ax.grid(alpha=0.3)
    if ax.lines and not rax:
        ax.legend(**LEGEND)
    fig.tight_layout()
    fig.savefig(path, dpi=100, bbox_inches='tight')
    plt.close(fig)
    return drawn > 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run_a')
    ap.add_argument('run_b')
    ap.add_argument('--label-a')
    ap.add_argument('--label-b')
    ap.add_argument('--name', help='folder name (default: cmp_<A>__<B>)')
    ap.add_argument('--out', default=os.path.expanduser('~/tiering_results'))
    ap.add_argument('--push', action='store_true')
    ap.add_argument('--no-png', action='store_true')
    a = ap.parse_args()
    la, lb = a.label_a or a.run_a, a.label_b or a.run_b

    info = []
    for run in (a.run_a, a.run_b):
        t0, t1, start = run_range(run)
        rows, labels, h0, h1 = summary(run, t0, t1)
        info.append((run, t0, t1, start, rows, labels, h0, h1))
    (_, _, _, sa, ra, laba, *ha), (_, _, _, sb, rb, labb, *hb) = info

    name = a.name or f'cmp_{a.run_a}__{a.run_b}'
    lines = [f'# {la} vs {lb}', '',
             f'| | A: {la} | B: {lb} |', '|---|---|---|']
    for item, f in (('run', lambda r, s, l, h, t0, t1: f'`{r}`'),
                    ('kind', lambda r, s, l, h, t0, t1: l.get('run_kind', '—')),
                    ('commit', lambda r, s, l, h, t0, t1: f'`{l.get("commit", "—")}`'),
                    ('blocks', lambda r, s, l, h, t0, t1: f'{fmt(h[0])} → {fmt(h[1])}'),
                    ('time', lambda r, s, l, h, t0, t1: f'{iso(t0)} → {iso(t1)}')):
        lines.append(f'| {item} | ' + ' | '.join(f(r, s, l, (h0, h1), t0, t1) for r, t0, t1, s, _, l, h0, h1 in info) + ' |')
    report = lambda r: f'[{r}/metrics.md](../{r}/metrics.md)' if os.path.exists(os.path.join(a.out, r, 'metrics.md')) else '—'
    lines += [f'| report | {report(a.run_a)} | {report(a.run_b)} |', '']
    for lab, s in ((la, sa), (lb, sb)):
        if s and s.get('flags'):
            lines += [f'Flags {lab}:', '', '```', s['flags'], '```', '']
    outdir = os.path.join(a.out, name)
    notes_path = os.path.join(outdir, 'notes.json')
    os.makedirs(outdir, exist_ok=True)
    if not os.path.exists(notes_path):
        json.dump({item: '' for item, _, _ in ra}, open(notes_path, 'w'), indent=1, ensure_ascii=False)
    notes = json.load(open(notes_path))
    lines += ['## Summary', '', 'B/A is the ratio of each value, in the same order as the values. Notes come from `notes.json` '
              '(metric name -> note) in this folder.', '',
              f'| Metric | A: {la} | B: {lb} | B/A | Notes |', '|---|---|---|---|---|']
    for (item, va, da), (_, vb, db) in zip(ra, rb):
        note = notes.get(item, '').replace('|', '\\|').replace('\n', '<br>')
        lines.append(f'| {item} | {da} | {db} | {" / ".join(ratio(x[0], y[0]) for x, y in zip(va, vb))} | {note} |')
    unknown = sorted(set(notes) - {item for item, _, _ in ra})
    if unknown:
        print('notes.json keys that match no metric:', *unknown, sep='\n  ')
    lines.append('')

    os.makedirs(os.path.join(outdir, 'images'), exist_ok=True)
    n = 0
    if not a.no_png:
        dash = json.load(open(f'{M}/dashboards/tv2.json'))
        runs = [(lab, run, t0, t1, height_at(run, t0, t1)) for lab, (run, t0, t1, *_) in zip((la, lb), info)]
        lines += ['## Graphs', '', f'Solid/dashed styles are series; color is the run (blue = {la}, orange = {lb}).', '']
        skipped = []
        for p in dash['panels']:
            if p['description'] in OMIT:
                continue
            if p['type'] != 'timeseries':
                skipped.append(p['title'])
                continue
            png = f'images/{p["description"]}.png'
            if plot_panel(p, runs, os.path.join(outdir, png)):
                n += 1
                lines += [f'### {p["title"]}', '', f'![{p["title"]}]({png})', '']
                if p['description'] in PANEL_NOTES:
                    lines += [f'*{PANEL_NOTES[p["description"]]}*', '']
            else:
                os.remove(os.path.join(outdir, png))
                skipped.append(p['title'])
        if skipped:
            lines += ['Not drawn (heatmaps or no data in both runs): ' + ', '.join(skipped) + '.', '']

    md = os.path.join(outdir, 'metrics.md')
    open(md, 'w').write('\n'.join(lines))
    print(f'wrote {md} and {n} PNGs')
    if a.push:
        push(a.out, name)


if __name__ == '__main__':
    main()
