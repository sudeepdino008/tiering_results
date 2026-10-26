#!/usr/bin/env python3
"""Write the report of one tiering v2 run (<run>.md + panel PNGs) into the results repo.
usage: tv2_report.py <run> [--name NAME] [--from TS] [--to TS] [--out DIR] [--push] [--no-png]
The range defaults to the run's start/stop marks in marks.jsonl. TS = unix seconds."""
import argparse, json, math, os, statistics, subprocess, time, urllib.parse, urllib.request

M = '/erigon-data/tv2_metrics'
PROM = 'http://127.0.0.1:9091'
GRAFANA = 'http://127.0.0.1:3000'


def prom(path, **params):
    url = f'{PROM}/api/v1/{path}?' + urllib.parse.urlencode(params)
    body = json.load(urllib.request.urlopen(url, timeout=60))
    if body['status'] != 'success':
        raise RuntimeError(body)
    return body['data']['result']


def run_range(run, frm=None, to=None):
    """(t0, t1, start mark) of a run, from its start/stop marks unless frm/to are given."""
    own = [m for m in (json.loads(l) for l in open(f'{M}/marks.jsonl')) if m.get('run') == run]
    start = next((m for m in own if m.get('event') == 'start'), None)
    stop = next((m for m in reversed(own) if m.get('event') == 'stop'), None)
    t0 = frm or (start and start['ts'])
    t1 = to or (stop and stop['ts']) or time.time()
    if not t0:
        raise SystemExit(f'no start mark for {run}; pass --from')
    return t0, t1, start


def fmt(v, unit=''):
    if v is None:
        return '—'
    if unit == 's':
        if v < 1e-3:
            return f'{v * 1e6:.1f} µs'
        return f'{v * 1000:.1f} ms' if v < 1 else f'{v:.2f} s'
    if unit == 'h':
        return f'{v:.2f} h'
    if unit == 'B':
        for u, d in (('TB', 1e12), ('GB', 1e9), ('MB', 1e6), ('KB', 1e3)):
            if abs(v) >= d:
                return f'{v / d:.2f} {u}'
        return f'{v:.0f} B'
    if unit == '%':
        return f'{v * 100:.2f}%'
    if v == int(v) or abs(v) >= 1000:
        return f'{v:,.0f}'
    return f'{v:,.2f}'


def text(vals, sep=' / '):
    return sep.join(fmt(v, u) for v, u in vals)


def summary(run, t0, t1):
    """Summary rows of a run: (item, [(value, unit), ...], display text)."""
    R = f'run="{run}"'
    rng = f'{max(int(t1 - t0), 60)}s'
    dur = t1 - t0

    def scalar(expr):
        res = prom('query', query=expr, time=t1)
        if not res:
            return None
        v = float(res[0]['value'][1])
        return None if math.isnan(v) or math.isinf(v) else v

    def series(expr, step=30):
        res = prom('query_range', query=expr, start=t0, end=t1, step=step)
        return [float(v) for r in res for _, v in r['values'] if v not in ('NaN', '+Inf', '-Inf')]

    def hq(metric, p, sel=R):
        return scalar(f'histogram_quantile({p}, sum by (le) (increase({metric}_bucket{{{sel}}}[{rng}])))')

    def hmean(metric, sel=R):
        return scalar(f'increase({metric}_sum{{{sel}}}[{rng}]) / increase({metric}_count{{{sel}}}[{rng}])')

    def ci95(metric):
        xs = series(f'rate({metric}_sum{{{R}}}[30s]) / rate({metric}_count{{{R}}}[30s])')
        if len(xs) < 2:
            return None
        return statistics.mean(xs), 1.96 * statistics.stdev(xs) / math.sqrt(len(xs)), len(xs)

    def div(x, y):
        return x / y if x is not None and y else None

    def dist(metric, unit, sel=R):
        return [(hq(metric, p, sel), unit) for p in (0.5, 0.9, 0.95, 0.99)]

    h0 = scalar(f'min(min_over_time((sync{{stage="execution",{R}}} > 0)[{rng}:10s]))')
    h1 = scalar(f'max(max_over_time(sync{{stage="execution",{R}}}[{rng}]))')
    blocks = (h1 - h0) if h0 is not None and h1 is not None else None
    per_block = lambda expr: div(scalar(expr), blocks)
    disk = lambda m, dev: per_block(f'increase({m}{{device="{dev}"}}[{rng}])')
    inc = lambda m: scalar(f'increase({m}{{{R}}}[{rng}])')
    rows = []

    def row(item, vals, display=None):
        rows.append((item, vals, display or text(vals)))

    def timing(name, metric, worst_metric):
        ci = ci95(metric)
        row(f'{name} p50 / p90 / p95 / p99', dist(metric, 's'))
        row(f'{name} worst', [(scalar(f'max_over_time({worst_metric}{{{R}}}[{rng}])'), 's')])
        vals = [(ci[0], 's'), (ci[1], 's')] if ci else [(None, 's'), (None, 's')]
        row(f'{name} mean ± 95% CI (30 s windows)', vals, f'{text(vals, " ± ")} (n={ci[2]})' if ci else '—')

    row('blocks executed', [(blocks, '')])
    row('wall time', [(dur / 3600, 'h')])
    row('blocks per second (mean)', [(div(blocks, dur), '')])
    row('Mgas/s per block mean / p50 / p5', [(hmean('exec_block_mgas_per_sec'), ''), (hq('exec_block_mgas_per_sec', 0.5), ''), (hq('exec_block_mgas_per_sec', 0.05), '')])
    row('Mgas/s wall clock (all-in)', [(div(inc('exec_gas_used_total'), dur * 1e6), '')])
    timing('exec time per block (exec + commitment)', 'exec_block_seconds', 'exec_block_seconds_max')
    timing('commitment time per block', 'commitment_round_duration_seconds', 'commitment_round_duration_seconds_max')
    for t in ('ssd', 'hdd', 'hdd_slow'):
        m = f'tiering_{t}_probes_per_block'
        row(f'{t.replace("_", " ")} probes per block mean / p50 / p90 / p95 / p99', [(hmean(m), '')] + dist(m, ''))
    row('share of probes on HDD', [(scalar(f'increase(tiering_file_probes_total{{tier="hdd",{R}}}[{rng}]) / ignoring(tier) sum without(tier) (increase(tiering_file_probes_total{{{R}}}[{rng}]))'), '%')])
    row('share of lookups that reached HDD', [(scalar(f'increase(tiering_hdd_lookups_total{{{R}}}[{rng}]) / increase(tiering_lookups_total{{{R}}}[{rng}])'), '%')])
    row('HDD probe latency p50 / p90 / p95 / p99', dist('tiering_file_probe_seconds', 's', f'tier="hdd",{R}'))
    row('SSD probe latency p50 / p90 / p95 / p99 (sampled)', dist('tiering_file_probe_seconds', 's', f'tier="ssd",{R}'))
    hdd_sel = f'tier="hdd",{R}'
    over = lambda n: div(scalar(f'increase(tiering_probes_per_lookup_count{{{hdd_sel}}}[{rng}]) - ignoring(le) increase(tiering_probes_per_lookup_bucket{{le="{n}",{hdd_sel}}}[{rng}])'),
                         scalar(f'increase(tiering_probes_per_lookup_count{{{hdd_sel}}}[{rng}])'))
    row('HDD probes per lookup that reached HDD: mean / share > 1 / share > 4', [(hmean('tiering_probes_per_lookup', hdd_sel), ''), (over(1), '%'), (over(4), '%')])
    row('existence-filter false positives (HDD / SSD)', [(scalar(f'increase(tiering_existence_false_positives_total{{tier="{t}",{R}}}[{rng}])'), '') for t in ('hdd', 'ssd')])
    for tier, kind, label in (('hdd', 'kv', 'data'), ('ssd', 'kv', 'data'), ('ssd', 'accessor', 'index')):
        row(f'commitment {label} size on {tier.upper()} (end)', [(scalar(f'last_over_time(tiering_commitment_bytes{{tier="{tier}",kind="{kind}",{R}}}[{rng}])'), 'B')])
    row('commitment data + index size, SSD + HDD (end)', [(scalar(f'sum(last_over_time(tiering_commitment_bytes{{{R}}}[{rng}]))'), 'B')])
    row('SSD space saved (commitment data on HDD) (end)', [(scalar(f'last_over_time(tiering_cold_resident_bytes{{domain="commitment",{R}}}[{rng}])'), 'B')])
    row('duplicate bytes (max)', [(scalar(f'max(max_over_time(tiering_duplicate_bytes{{{R}}}[{rng}]))'), 'B')])
    for reason in ('straddling_file', 'copy_pending'):
        sel = f'domain="commitment",reason="{reason}",{R}'
        row(f'movement lag, {reason} (blocks: max / end)', [(scalar(f'max_over_time(tiering_lag_blocks{{{sel}}}[{rng}])'), ''), (scalar(f'last_over_time(tiering_lag_blocks{{{sel}}}[{rng}])'), '')])
    row('HDD end block / SSD start block (end)', [(scalar(f'last_over_time({m}{{domain="commitment",{R}}}[{rng}])'), '') for m in ('tiering_hdd_end_block', 'tiering_ssd_start_block')])
    row('cold merges: count / total seconds / paused seconds', [(inc('tiering_cold_merge_seconds_count'), ''), (inc('tiering_cold_merge_seconds_sum'), 's'), (inc('tiering_cold_merge_paused_seconds_total'), 's')])
    row('cold merges: bytes read / written', [(inc('tiering_cold_merge_in_bytes_total'), 'B'), (inc('tiering_cold_merge_out_bytes_total'), 'B')])
    row('major page faults per block', [(per_block(f'increase(process_major_pagefaults_total{{{R}}}[{rng}])'), '')])
    for tier, dev in (('hdd', 'sda'), ('ssd', 'nvme0n1')):
        row(f'{tier} reads per block / read bytes per block', [(disk('node_disk_reads_completed_total', dev), ''), (disk('node_disk_read_bytes_total', dev), 'B')])
        io = scalar(f'increase(node_disk_io_time_seconds_total{{device="{dev}"}}[{rng}])')
        r_await = div(scalar(f'increase(node_disk_read_time_seconds_total{{device="{dev}"}}[{rng}])'), scalar(f'increase(node_disk_reads_completed_total{{device="{dev}"}}[{rng}])'))
        row(f'{tier} r_await (mean) / utilization (mean)', [(r_await, 's'), (div(io, dur), '%')])
    labels = (prom('query', query=f'last_over_time(up{{{R}}}[{rng}])', time=t1) or [{'metric': {}}])[0]['metric']
    return rows, labels, h0, h1


iso = lambda t: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t))


def push(out, name):
    subprocess.run(['git', '-C', out, 'add', name], check=True)
    subprocess.run(['git', '-C', out, 'commit', '-qm', f'report: {name}'], check=True)
    subprocess.run(['git', '-C', out, 'push', '-q'], check=True)
    print('pushed')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run')
    ap.add_argument('--from', dest='frm', type=float)
    ap.add_argument('--to', type=float)
    ap.add_argument('--out', default=os.path.expanduser('~/tiering_results'))
    ap.add_argument('--push', action='store_true')
    ap.add_argument('--no-png', action='store_true')
    ap.add_argument('--name', help='report folder/file name (default: the run label)')
    a = ap.parse_args()

    t0, t1, start = run_range(a.run, a.frm, a.to)
    rows, labels, h0, h1 = summary(a.run, t0, t1)
    lines = [f'# {a.name or a.run}', '',
             '| | |', '|---|---|',
             f'| kind | {labels.get("run_kind", "—")} |',
             f'| datadir | `{labels.get("datadir") or (start or {}).get("datadir", "—")}` |',
             f'| commit | `{labels.get("commit", "—")}` |',
             *([f'| metrics run label | `{a.run}` |'] if a.name and a.name != a.run else []),
             f'| blocks | {fmt(h0)} → {fmt(h1)} |',
             f'| time | {iso(t0)} → {iso(t1)} |', '']
    if start and start.get('flags'):
        lines += ['Flags:', '', '```', start['flags'], '```', '']
    lines += ['## Summary', '', '| Metric | Value |', '|---|---|'] + [f'| {i} | {d} |' for i, _, d in rows] + ['']

    name = a.name or a.run
    rundir = os.path.join(a.out, name)
    os.makedirs(os.path.join(rundir, 'images'), exist_ok=True)
    pngs = []
    if not a.no_png:
        dash = json.load(open(f'{M}/dashboards/tv2.json'))
        auth = 'Bearer ' + open(f'{M}/grafana_token').read().strip()
        lines += ['## Graphs', '']
        for p in dash['panels']:
            png = f'images/{p["description"]}.png'
            url = f'{GRAFANA}/render/d-solo/{dash["uid"]}/x?' + urllib.parse.urlencode(
                {'panelId': p['id'], 'width': 1000, 'height': 400, 'theme': 'light', 'var-run': a.run,
                 'from': int((t0 - 60) * 1000), 'to': int((t1 + 60) * 1000), 'tz': 'UTC'})
            req = urllib.request.Request(url, headers={'Authorization': auth})
            with open(os.path.join(rundir, png), 'wb') as f:
                f.write(urllib.request.urlopen(req, timeout=120).read())
            pngs.append(png)
            lines += [f'### {p["title"]}', '', f'![{p["title"]}]({png})', '']

    md = os.path.join(rundir, 'metrics.md')
    open(md, 'w').write('\n'.join(lines))
    print(f'wrote {md} and {len(pngs)} PNGs')
    if a.push:
        push(a.out, name)


if __name__ == '__main__':
    main()
