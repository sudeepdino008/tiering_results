#!/erigon-data/tv2_scripts/.venv/bin/python
"""Stage 17 matrix helpers.
usage: tv2_matrix_report.py layout <datadir>                      -> markdown on stdout
       tv2_matrix_report.py stats <cell dir> <run> <datadir> <L> <M> <rc>  -> <cell dir>/stats.json
       tv2_matrix_report.py report [--mx DIR]                     -> runs.csv, frontier/trends/progress PNG+SVG, README.md"""
import argparse, csv, glob, json, os, re, sys, time

MX = '/home/moskud/tiering_results/matrix_run/2026-11-16'
STEP = 390625
LS = ['1mo', '3mo', '4mo', '6mo']
W1 = 25400000
TREND_LS = LS + ['9mo@W2']
GRID_LS = LS + ['6mo@W2', '9mo@W2']
MS = [1, 4, 32, 64, 128]
LB = {'1mo': 216000, '3mo': 648000, '4mo': 864000, '6mo': 1296000, '9mo': 1944000}
L_COLOR = {'1mo': '#2a78d6', '3mo': '#eb6834', '4mo': '#1baf7a', '6mo': '#eda100'}
L_COLOR.update({'6mo@W2': L_COLOR['6mo'], '9mo@W2': '#d55181'})
M_COLOR = dict(zip(MS, ['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#d55181']))
STEP_H = 1520 * 12 / 3600  # one step ≈ 1,520 blocks near W at 12 s per block


def mlab(m):
    h = m * STEP_H
    return f"M={m} (~{h:.0f} h)" if h < 24 else f"M={m} (~{h / 24:.0f} d)"


M_RADIUS = {1: 5, 4: 6.5, 32: 8, 64: 9.5, 128: 11}
INK, INK2, MUTED, GRID, SURFACE, CRIT = '#141412', '#52514e', '#898781', '#e1e0d9', '#fcfcfb', '#d03b3b'
BASELINE = {'mgas_s_per_block': 277, 'commit_p50_ms': 22.4, 'commit_p95_ms': 73.4, 'commit_p99_ms': 135.6, 'ssd_commit_gb': 300, 'name': 'baseline_allssd_merged_6mo_w25400000_2026-10-23-3'}
FRONTIERS = [('mgas', 'mgas_s_per_block', 'Mgas/s per block (higher is better)', True),
             ('p50', 'commit_p50_ms', 'commitment p50 ms per block (lower is better)', False),
             ('p99', 'commit_p99_ms', 'commitment p99 ms per block (lower is better)', False)]
COLS = ['order', 'L', 'W', 'lookback_blocks', 'M', 'mgas_s_per_block', 'wall_mgas_s', 'commit_p50_ms', 'commit_p95_ms', 'commit_p99_ms',
        'ssd_commit_gb', 'hdd_commit_gb', 'hot_files', 'ssd_probes_per_block', 'hdd_probes_per_block', 'hdd_probe_share',
        'demotions', 'demoted_gb', 'cold_merges', 'duration_s', 'oom_kill', 'memory_peak_gb']
GEOMETRY = """| L | boundary block / step | cold set on HDD (besides 0-8192) | HDD GB | hot steps on SSD | 1-step hot GB |
|---|---|---|---|---|---|
| 6mo | 24,104,000 / 8199 | 8192-8196, 8196-8198 | ~186 | 1,043 | ~730 |
| 4mo | 24,536,000 / ~8543 | 8192-8448, 8448-8512, 8512-8528, +8+4+2+1 | ~225 | ~700 | ~490 |
| 3mo | 24,752,000 / 8714 | 8192-8448, 8448-8704, 8704-8712, 8712-8714 | ~248 | 528 | ~370 |
| 1mo | 25,184,000 / ~9066 | 8192-8448, 8448-8704, 8704-8960, 8960-9024, 9024-9056, +8+2 | ~290 | ~176 | ~125 |"""


def commitment_files(dd):
    """(name, from step, to step, bytes, tier) of every commitment .kv in the datadir; symlinks are HDD."""
    out = []
    for p in glob.glob(f'{dd}/snapshots/domain/v*-commitment.*.kv'):
        m = re.search(r'\.(\d+)-(\d+)\.kv$', p)
        out.append((os.path.basename(p), int(m[1]), int(m[2]), os.stat(p).st_size, 'HDD' if os.path.islink(p) else 'SSD'))
    return sorted(out, key=lambda f: f[1])


def layout(dd):
    files = commitment_files(dd)
    bnd = open(f'{dd}/TV2_README.md').read()
    m = re.search(r'cold boundary: block (\d+), min_txnum (\d+), step (\d+)', bnd)
    lines = [f'# Commitment layout of `{dd}` at {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}', '',
             f'Cold boundary: block {int(m[1]):,}, step {m[3]}. Blocks per step near W ≈ 1,520, so a 10,000-block run '
             f'adds ~6.6 steps.', '', '| tier | files | bytes | steps |', '|---|---|---|---|']
    for tier in ('SSD', 'HDD'):
        fs = [f for f in files if f[4] == tier]
        lines.append(f'| {tier} | {len(fs)} | {sum(f[3] for f in fs) / 1e9:,.1f} GB | {sum(f[2] - f[1] for f in fs):,} |')
    lines += ['', '| file | steps | bytes | tier |', '|---|---|---|---|']
    lines += [f'| {n} | {b - a} | {s:,} | {t} |' for n, a, b, s, t in files]
    return '\n'.join(lines) + '\n'


def stats(cell, run, dd, L, M, rc, W=W1):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import tv2_report as R
    st = {'run': run, 'L': L, 'lookback_blocks': LB[L], 'M': int(M), 'rc': int(rc), 'datadir': dd, 'W': int(W)}
    out = f'{dd}/logs/run.out'
    log = open(out, errors='replace').read() if os.path.exists(out) else ''
    st['root_errors'] = len(re.findall(r'Wrong trie root', log))
    blk = re.findall(r'blk=(\d+)', log)
    st['last_block'] = int(blk[-1]) if blk else None
    if int(rc) != 0:
        st['error_excerpt'] = '\n'.join(l for l in log.splitlines()[-400:] if re.search(r'EROR|ERR|panic|fatal', l))[-3000:]
    mem = f'{dd}/logs/memcg.txt'
    peak, oom, mmax = 0, 0, None
    if os.path.exists(mem):
        for l in open(mem):
            if l.startswith('cgroup'):
                mmax = int(l.split()[-1]) if l.split()[-1].isdigit() else l.split()[-1]
                continue
            w = l.split()
            if len(w) >= 3 and w[2].isdigit():
                peak = max(peak, int(w[2]))
            ev = dict(zip(w[3::2], w[4::2]))
            oom = max(oom, int(ev.get('oom_kill', 0)))
    st['memory_max'] = mmax
    st['memory_peak_gb'] = round(peak / 2**30, 2)
    st['oom_kill'] = 1 if int(rc) == 137 else oom
    files = commitment_files(dd)
    st['hot_files'] = sum(1 for f in files if f[4] == 'SSD')
    st['layout_after'] = {t: [len([f for f in files if f[4] == t]), sum(f[3] for f in files if f[4] == t)] for t in ('SSD', 'HDD')}
    try:
        t0, t1, _ = R.run_range(run)
        rows = {i: v for i, v, _ in R.summary(run, t0, t1)[0]}
        g = lambda k, i=0: rows[k][i][0]
        gb = lambda v: None if v is None else round(v / 1e9, 2)
        ms = lambda v: None if v is None else round(v * 1000, 1)
        st.update(mgas_s_per_block=g('Mgas/s per block mean / p50 / p5'), mgas_s_p50=g('Mgas/s per block mean / p50 / p5', 1),
                  wall_mgas_s=g('Mgas/s wall clock (all-in)'),
                  commit_p50_ms=ms(g('commitment time per block p50 / p90 / p95 / p99')),
                  commit_p95_ms=ms(g('commitment time per block p50 / p90 / p95 / p99', 2)),
                  commit_p99_ms=ms(g('commitment time per block p50 / p90 / p95 / p99', 3)),
                  ssd_commit_gb=gb(g('commitment data size on SSD (end)')), hdd_commit_gb=gb(g('commitment data size on HDD (end)')),
                  ssd_probes_per_block=g('ssd probes per block mean / p50 / p90 / p95 / p99'),
                  hdd_probes_per_block=g('hdd probes per block mean / p50 / p90 / p95 / p99'),
                  hdd_probe_share=g('share of probes on HDD'), cold_merges=round(g('cold merges: count / total seconds / paused seconds') or 0),
                  blocks=g('blocks executed'), duration_s=round(t1 - t0))
        inc = lambda m: R.prom('query', query=f'increase({m}{{run="{run}"}}[{max(int(t1 - t0), 60)}s])', time=t1)
        d, b = inc('tiering_demotions_total'), inc('tiering_demoted_bytes_total')
        st['demotions'] = round(sum(float(r['value'][1]) for r in d)) if d else 0
        st['demoted_gb'] = round(sum(float(r['value'][1]) for r in b) / 1e9, 2) if b else 0
    except Exception as e:  # a failed cell may have no marks or metrics; keep what the logs give
        st['metrics_error'] = repr(e)[:500]
    json.dump(st, open(f'{cell}/stats.json', 'w'), indent=1)
    print(json.dumps({k: v for k, v in st.items() if k != 'error_excerpt'}))


def load(mx):
    order = [l.split() for l in open(f'{mx}/order.txt') if l[0].isdigit()]
    rows = {}
    for p in glob.glob(f'{mx}/cells/*/stats.json'):
        s = json.load(open(p))
        rows[(s['L'] + ('@W2' if s.get('W', W1) != W1 else ''), s['M'])] = s
    running = open(f'{mx}/running.txt').read().split() if os.path.exists(f'{mx}/running.txt') else []
    return order, rows, (running[0] + ('@W2' if running[2:] == ['w2'] else ''), int(running[1])) if len(running) >= 2 else None


def ok(s):
    return s and s['rc'] == 0 and s.get('mgas_s_per_block') is not None


def style(ax, xlabel, ylabel):
    ax.grid(color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    for sp in ('left', 'bottom'):
        ax.spines[sp].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.set_xlabel(xlabel, color=INK2, fontsize=10)
    ax.set_ylabel(ylabel, color=INK2, fontsize=10)


def pareto(pts, y_better_high):
    """Non-dominated points for min x and best y."""
    best, front = None, []
    for p in sorted(pts, key=lambda p: (p[0], -p[1] if y_better_high else p[1])):
        if best is None or (p[1] > best if y_better_high else p[1] < best):
            front.append(p)
            best = p[1]
    return front


def place_labels(ax, pts, front):
    """Label each point with its M (colour = lookback; frontier labels bold); try right/above/below/left, else stack downwards."""
    ax.figure.canvas.draw()
    disp = {p: ax.transData.transform(p[:2]) for p in pts}
    boxes = [(x - r, y - r, x + r, y + r) for p, (x, y) in disp.items() for r in [M_RADIUS[p[3]] * 1.1]]
    clash = lambda b: any(b[0] < c[2] and c[0] < b[2] and b[1] < c[3] and c[1] < b[3] for c in boxes)
    for p in sorted(pts, key=lambda p: (-p[1], p[0])):
        px, py = disp[p]
        t, on = mlab(p[3]).split('(')[1].rstrip(')'), p in front
        probe = ax.text(0, 0, t, fontsize=8, fontweight='bold' if on else 'normal')
        bb = probe.get_window_extent(ax.figure.canvas.get_renderer())
        probe.remove()
        w, h, r = bb.width + 3, bb.height + 1, M_RADIUS[p[3]] * 1.1 + 2
        cands = [(r, -h / 2), (-w / 2, r), (-w / 2, -r - h), (-r - w, -h / 2)] + \
                [(dx, -h / 2 + sgn * k * (h + 2)) for k in range(1, 8) for sgn in (-1, 1) for dx in (r, -r - w)]
        dx, dy = next(((dx, dy) for dx, dy in cands if not clash((px + dx, py + dy, px + dx + w, py + dy + h))), cands[0])
        boxes.append((px + dx, py + dy, px + dx + w, py + dy + h))
        ax.annotate(t, p[:2], xytext=(dx * 72 / ax.figure.dpi, (dy + h / 2) * 72 / ax.figure.dpi), textcoords='offset points', fontsize=8, va='center',
                    color=L_COLOR[p[2]] if not on else INK, fontweight='bold' if on else 'normal',
                    arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.5) if abs(dy) > r + h else None)


def save(fig, mx, name):
    for ext in ('png', 'svg'):
        fig.savefig(f'{mx}/{name}.{ext}', dpi=200 if ext == 'png' else None, facecolor=SURFACE, bbox_inches='tight')


def charts(mx, rows, running, n):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    done = {k: s for k, s in rows.items() if ok(s)}

    def frontier(ax, key, label, high):
        ax.set_facecolor(SURFACE)
        pts = [(s['ssd_commit_gb'], s[key], L, M) for (L, M), s in done.items() if s.get(key) is not None and s.get('ssd_commit_gb')]
        front = pareto(pts, high)
        for x, y, L, M in pts:
            ax.scatter(x, y, s=(2 * M_RADIUS[M]) ** 2 * 0.55, color=L_COLOR[L], marker='D' if '@W2' in L else 'o', edgecolor=SURFACE, linewidth=2,
                       alpha=1 if (x, y, L, M) in front else 0.75, zorder=3)
        if len(front) > 1:
            ax.plot([p[0] for p in front], [p[1] for p in front], ls='--', color=INK2, lw=1, zorder=4)
        if key in BASELINE:
            ax.scatter(BASELINE['ssd_commit_gb'], BASELINE[key], marker='s', s=70, facecolor='none', edgecolor=INK2, zorder=3)
            ax.annotate(f'all-SSD baseline ({BASELINE[key]:g})', (BASELINE['ssd_commit_gb'], BASELINE[key]), xytext=(6, -12), textcoords='offset points', fontsize=8, color=INK2)
        ax.axvline(BASELINE['ssd_commit_gb'], color=MUTED, lw=0.8, ls=':')
        style(ax, 'SSD commitment GB at run end (lower is better)', label)
        place_labels(ax, pts, front)

    handles = [Line2D([], [], marker='D' if '@W2' in L else 'o', ls='', color=L_COLOR[L], label=L) for L in GRID_LS if any(k[0] == L for k in rows) or L in LS] + \
              [Line2D([], [], marker='o', ls='', color=MUTED, markersize=M_RADIUS[M] * 0.9, label=mlab(M)) for M in MS] + \
              [Line2D([], [], marker='s', ls='', markerfacecolor='none', color=INK2, label='baseline')]
    sub = '(colour = lookback, label = M as time span, dashed = Pareto frontier)'
    fig, axes = plt.subplots(1, 3, figsize=(19, 5.2), facecolor=SURFACE)
    for ax, f in zip(axes, FRONTIERS):
        frontier(ax, *f[1:])
    fig.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, 0.97), ncol=len(handles), frameon=False, fontsize=8, columnspacing=1.2, handletextpad=0.3)
    fig.suptitle(f'Lookback × SSD merge limit: SSD cost vs speed {sub}', y=1.08, color=INK, fontsize=12)
    save(fig, mx, 'frontier')
    plt.close(fig)
    for name, key, label, high in FRONTIERS:
        fig, ax = plt.subplots(figsize=(11, 7), facecolor=SURFACE)
        frontier(ax, key, label, high)
        fig.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, 0.89), ncol=len(handles), frameon=False, fontsize=9, columnspacing=1.2, handletextpad=0.3)
        fig.suptitle(f'SSD cost vs {label.split(" (")[0]} {sub}', y=0.95, color=INK, fontsize=12)
        save(fig, mx, f'frontier_{name}')
        plt.close(fig)

    fig, axes = plt.subplots(2, 2, figsize=(13, 8.2), facecolor=SURFACE)
    for r, (key, label) in enumerate([('ssd_commit_gb', 'SSD commitment GB'), ('mgas_s_per_block', 'Mgas/s per block')]):
        for c, (xs, lines, xname, colors, getk) in enumerate([
                (TREND_LS, MS, 'lookback (9mo only at W2)', M_COLOR, lambda x, ln: (x, ln)), (MS, TREND_LS, 'SSD merge limit M (steps)', L_COLOR, lambda x, ln: (ln, x))]):
            ax = axes[r][c]
            ax.set_facecolor(SURFACE)
            for ln in lines:
                ys = [done[getk(x, ln)][key] if getk(x, ln) in done else None for x in xs]
                ax.plot(range(len(xs)), [float('nan') if y is None else y for y in ys], color=colors[ln], lw=2, marker='o',
                        markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5, label=mlab(ln) if c == 0 else ln)
                for i, x in enumerate(xs):
                    s = rows.get(getk(x, ln))
                    if s and not ok(s):
                        ax.scatter(i, ax.get_ylim()[0], marker='o', facecolor='none', edgecolor=colors[ln], zorder=3)
            ax.set_xticks(range(len(xs)), [mlab(x).replace(' (', '\n(') if c == 1 else str(x) for x in xs])
            style(ax, xname, label)
    h = [Line2D([], [], color=M_COLOR[M], lw=2, label=mlab(M)) for M in MS] + [Line2D([], [], color=L_COLOR[L], lw=2, label=L) for L in TREND_LS]
    fig.tight_layout()
    fig.legend(handles=h, loc='lower center', bbox_to_anchor=(0.5, 1.0), ncol=5, frameon=False, fontsize=9)
    fig.suptitle('Trends: left by lookback (lines = M), right by merge limit (lines = lookback)', y=1.1, color=INK, fontsize=12)
    save(fig, mx, 'trends')
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.2), facecolor=SURFACE)
    seq = plt.get_cmap('Blues')
    vals = [s['mgas_s_per_block'] for s in done.values()]
    lo, hi = (min(vals), max(vals)) if vals else (0, 1)
    for i, L in enumerate(GRID_LS):
        for j, M in enumerate(MS):
            s = rows.get((L, M))
            y = len(GRID_LS) - 1 - i
            if ok(s):
                v = s['mgas_s_per_block']
                f = 0.35 + 0.55 * ((v - lo) / (hi - lo) if hi > lo else 0.5)
                ax.add_patch(plt.Rectangle((j, y), 0.95, 0.9, color=seq(f)))
                ax.text(j + 0.475, y + 0.45, f'{v:.0f}', ha='center', va='center', color='white' if f > 0.6 else INK, fontsize=11)
            elif s:
                ax.add_patch(plt.Rectangle((j, y), 0.95, 0.9, color=CRIT))
                ax.text(j + 0.475, y + 0.45, '×', ha='center', va='center', color='white', fontsize=14)
            else:
                run = running == (L, M)
                ax.add_patch(plt.Rectangle((j, y), 0.95, 0.9, facecolor=SURFACE, edgecolor='#1c5cab' if run else GRID, lw=2.5 if run else 1))
                ax.text(j + 0.475, y + 0.45, 'running' if run else '', ha='center', va='center', color='#1c5cab', fontsize=9)
    ax.set_xlim(0, len(MS))
    ax.set_ylim(0, len(GRID_LS))
    ax.set_xticks([j + 0.475 for j in range(len(MS))], [mlab(M).replace(' (', '\n(') for M in MS])
    ax.set_yticks([len(GRID_LS) - 1 - i + 0.45 for i in range(len(GRID_LS))], GRID_LS)
    ax.tick_params(length=0, colors=INK2)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(f'Matrix progress: {len(done)}/{n} done (number = Mgas/s per block)', color=INK, fontsize=11)
    save(fig, mx, 'progress')
    plt.close(fig)


def fmtv(v, nd=1):
    if v is None:
        return '—'
    if isinstance(v, float):
        return f'{v:,.{nd}f}'
    return f'{v:,}' if isinstance(v, int) else str(v)


def report(mx):
    order, rows, running = load(mx)
    sk = lambda o: o[2] + ('@W2' if o[5:] == ['w2'] else '')
    idx = {(sk(o), int(o[3])): int(o[0]) for o in order}
    with open(f'{mx}/runs.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(COLS + ['rc', 'root_errors'])
        for k in sorted(rows, key=lambda k: idx.get(k, 99)):
            s = dict(rows[k], order=idx.get(k))
            w.writerow([s.get(c) for c in COLS + ['rc', 'root_errors']])
    charts(mx, rows, running, len(order))
    table = ['| # | L | M | Mgas/s per block | wall Mgas/s | commit p50 / p95 / p99 ms | SSD GB | HDD GB | hot files | SSD / HDD probes per block | '
             'demotions (GB) | cold merges | duration h | rc / root err / OOM / peak GiB |', '|' + '---|' * 14]
    for o in order:
        k = (sk(o), int(o[3]))
        s = rows.get(k)
        cell = f'[{k[0]}/{o[3]}](cells/{o[2]}_m{o[3]}{"_w2" if "@W2" in k[0] else ""}/)'
        if not s:
            table.append(f'| {o[0]} | {k[0]} | {o[3]} | {"running" if running == k else "pending"} |' + ' |' * 10)
            continue
        dur = s.get('duration_s')
        table.append(f'| {o[0]} | {cell} | {o[3]} | {fmtv(s.get("mgas_s_per_block"))} | {fmtv(s.get("wall_mgas_s"))} | '
                     f'{fmtv(s.get("commit_p50_ms"))} / {fmtv(s.get("commit_p95_ms"))} / {fmtv(s.get("commit_p99_ms"))} | {fmtv(s.get("ssd_commit_gb"))} | '
                     f'{fmtv(s.get("hdd_commit_gb"))} | {fmtv(s.get("hot_files"))} | {fmtv(s.get("ssd_probes_per_block"), 0)} / '
                     f'{fmtv(s.get("hdd_probes_per_block"), 0)} | {fmtv(s.get("demotions"))} ({fmtv(s.get("demoted_gb"))}) | '
                     f'{fmtv(s.get("cold_merges"), 0)} | {fmtv(dur / 3600 if dur else None, 2)} | '
                     f'{s["rc"]} / {s.get("root_errors")} / {s.get("oom_kill")} / {fmtv(s.get("memory_peak_gb"))} |')
    concl = open(f'{mx}/conclusions.md').read() if os.path.exists(f'{mx}/conclusions.md') else ''
    readme = f"""# Matrix run: lookback × SSD merge limit (stage 17)

Updated {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}. {len([r for r in rows.values() if ok(r)])}/{len(order)} cells done{f', running {running[0]}/{running[1]}' if running else ''}.

Each cell: 10,000 chaintip blocks 25,400,001..25,410,000 from W = 25,400,000, demotion on, offline BALs, state cache on,
`--tiering.cold-io-max-mbps=50`, erigon c604cf14, 64 GiB memory scope (page cache included), page caches dropped before the start.
L = lookback (cold boundary = W − L), M = SSD merge limit for commitment files (`--tiering.commitment-hot-merge-steps`).
Cold files are pre-merged and on HDD; hot files on SSD are merged up to M steps. All-SSD baseline (256-step merges):
{BASELINE['mgas_s_per_block']} Mgas/s per block, SSD commitment ≈ {BASELINE['ssd_commit_gb']} GB (`{BASELINE['name']}`).
Mgas/s per block = mean of the per-block value; SSD/HDD GB = commitment `.kv` bytes per tier at the run end.

### W2 (second start block, for 9mo)

W2 = 26,130,000. Cells marked `@W2` (diamonds in the frontier) run blocks 26,130,001..26,140,000 from base `tv2_1s_base_w2`.
Commitment data below block 24,091,854 is one 180 GB file (0-8192), and tiering moves only whole files. At W the 9mo boundary
is 25,400,000 − 1,944,000 = 23,456,000, inside that file, so nothing could go to HDD. At W2 it is 24,186,000, above it.
`6mo@W2/32` is the anchor: compared with `6mo/32` at W, it shows how much the block range alone changes the numbers.
12mo would need W2 ≥ ~26.69M, beyond the data on this box (ends at 26,147,580).

{concl}
## Charts

![frontier: Mgas/s](frontier_mgas.png)

![frontier: commitment p50](frontier_p50.png)

![frontier: commitment p99](frontier_p99.png)

![trends](trends.png)

![progress](progress.png)

## Cells (in run order, `order.txt`)

{chr(10).join(table)}

Data: [`runs.csv`](runs.csv). Each cell folder has `layout_before.md`, `stats.json`, `metrics.md` + `images/`, and logs.

## Geometry (plan estimates; the real boundary is in each cell's `layout_before.md`)

{GEOMETRY}
"""
    open(f'{mx}/README.md', 'w').write(readme)
    print(f'wrote {mx}/README.md, runs.csv and charts ({len(rows)} cells)')


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == 'layout':
        sys.stdout.write(layout(args[0]))
    elif cmd == 'stats':
        stats(*args)
    elif cmd == 'report':
        ap = argparse.ArgumentParser()
        ap.add_argument('--mx', default=MX)
        report(ap.parse_args(args).mx)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
