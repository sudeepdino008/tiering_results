#!/usr/bin/env python3
"""Pre-run datadir check for the tiering v2 runs (see "Pre-run datadir check" in tiering_plan.md).

usage: precheck.py <datadir> --layout ssd|hdd0|tiered [--cold-dir DIR --boundary-step N] [--stop-block N] [--bal-dir DIR --bal-from N]
                   [--integration BIN --expect-exec N] [--min-free-gb N]
Prints one line per check, writes the same text to <datadir>/logs/precheck_<UTC ts>.txt, exits 1 on any FAIL.
"""
import argparse, os, re, shutil, struct, subprocess, sys, time

HDD_MOUNT, SSD_MOUNT = '/backup', '/'
HDD0 = {'snapshots/domain/v2.2-commitment.0-8192.kv':
        ('/backup/erigon-hdd/domain/v2.2-commitment.0-8192.kv', 180_470_634_040)}

ap = argparse.ArgumentParser()
ap.add_argument('datadir')
ap.add_argument('--layout', required=True, choices=['ssd', 'hdd0', 'tiered'])
ap.add_argument('--cold-dir', default='/backup/erigon-hdd/domain', help='tiered: the --tiering.cold-dir of the run')
ap.add_argument('--no-hdd0', action='store_true', help='tiered: the datadir has no 0-8192 commitment symlink (mn_bal_gen mirrors)')
ap.add_argument('--boundary-step', type=int, help='tiered: cold boundary step; no symlinked file may start at or above it')
ap.add_argument('--stop-block', type=int)
ap.add_argument('--bal-dir')
ap.add_argument('--bal-from', type=int)
ap.add_argument('--integration')
ap.add_argument('--expect-exec', type=int)
ap.add_argument('--min-free-gb', type=int, default=100)
a = ap.parse_args()
dd = os.path.abspath(a.datadir)
out, fails = [], 0


def report(ok, name, detail=''):
    global fails
    fails += not ok
    out.append(f"{'OK  ' if ok else 'FAIL'} {name}: {detail}")


def mount_of(p):
    return subprocess.run(['df', '--output=target', p], capture_output=True, text=True).stdout.split()[-1]


def check_tiered(links):
    """Demoted layout: only commitment .kv symlinks into the cold dir, accessors on SSD, no demotion leftovers."""
    cold = os.path.abspath(a.cold_dir)
    kv_re = re.compile(r'^snapshots/domain/(v[\d.]+-commitment\.(\d+)-(\d+))\.kv$')
    base0 = 'snapshots/domain/v2.2-commitment.0-8192.kv'
    if not a.no_hdd0:
        report(base0 in links, 'tiered: 0-8192 commitment is a symlink', links.get(base0, 'missing'))
    straddling = 0
    for rel, t in sorted(links.items()):
        m = kv_re.match(rel)
        p = os.path.join(dd, rel)
        if not m:
            report(False, f'tiered: unexpected symlink {rel}', t)
            continue
        size = os.path.getsize(p) if os.path.exists(p) else -1
        want_dir = cold
        ok = (os.path.isabs(t) and os.path.dirname(t) == want_dir and os.path.exists(p) and mount_of(t) == HDD_MOUNT
              and size > 0 and not os.path.exists(t + '.tmp'))
        if rel in HDD0:
            ok = ok and size == HDD0[rel][1]
        kvis = [f for f in os.listdir(os.path.dirname(p)) if f.endswith(m.group(1).split('-', 1)[1] + '.kvi')]
        kvi_ok = bool(kvis) and all(not os.path.islink(os.path.join(os.path.dirname(p), f)) and
                                    os.stat(os.path.join(os.path.dirname(p), f)).st_dev == os.stat(SSD_MOUNT).st_dev for f in kvis)
        fr, to = int(m.group(2)), int(m.group(3))
        if a.boundary_step is not None and fr < a.boundary_step < to:
            straddling += 1
        newer = a.boundary_step is not None and fr >= a.boundary_step
        report(ok and kvi_ok and not newer, f'tiered: symlink {rel}',
               f'-> {t}, size={size}, kvi on SSD={kvi_ok}, newer than boundary={newer}')
    report(straddling <= 1, 'tiered: at most one symlinked file straddles the boundary', f'{straddling}')
    dom = os.path.join(dd, 'snapshots/domain')
    left = [f for f in os.listdir(dom) if f.endswith('.demote.tmp')]
    own = {f + '.tmp' for f in os.listdir(dom) if '-commitment.' in f and f.endswith('.kv')}
    left += [os.path.join(cold, f) for f in os.listdir(cold) if f in own] if os.path.isdir(cold) else []
    report(not left, 'tiered: no demotion leftovers (*.demote.tmp, own .tmp in cold dir)', f'{left[:3]}')


report(dd.startswith('/erigon-data/'), 'datadir under /erigon-data', dd)
mdbx = os.path.join(dd, 'chaindata/mdbx.dat')
busy = subprocess.run(['fuser', mdbx], capture_output=True, text=True).stdout.strip()
report(os.path.exists(mdbx) and not busy, 'chaindata exists and is not in use', busy and f'pids {busy}')

expected = HDD0 if a.layout == 'hdd0' else {}
links = {}
for root, dirs, files in os.walk(dd):
    for n in dirs + files:
        p = os.path.join(root, n)
        if os.path.islink(p):
            links[os.path.relpath(p, dd)] = os.readlink(p)
if a.layout == 'tiered':
    check_tiered(links)
else:
    report(set(links) == set(expected), f'symlink set == layout {a.layout}', f'found {sorted(links) or "none"}')
for rel, (target, size) in expected.items():
    p = os.path.join(dd, rel)
    if rel not in links:
        continue
    t = links[rel]
    ok = (t == target and os.path.isabs(t) and os.path.exists(p) and mount_of(t) == HDD_MOUNT
          and os.path.getsize(p) == size)
    report(ok, f'symlink {rel}', f'-> {t}, resolves={os.path.exists(p)}, mount={mount_of(t) if os.path.exists(t) else "-"}, '
                                 f'size={os.path.getsize(p) if os.path.exists(p) else "-"}')

snap = os.path.join(dd, 'snapshots')
ssd_dev = os.stat(SSD_MOUNT).st_dev
off_ssd = [os.path.relpath(os.path.join(r, f), dd) for r, _, fs in os.walk(snap) for f in fs
           if not os.path.islink(os.path.join(r, f)) and os.stat(os.path.join(r, f)).st_dev != ssd_dev]
report(not off_ssd, 'all other snapshot files are regular files on SSD', f'{len(off_ssd)} not on SSD {off_ssd[:3]}')

name_re = re.compile(r'^v[\d.]+-([a-z]+)\.(\d+)-(\d+)\.(kv|kvi|bt|kvei)$')
kv, acc = {}, set()
for f in os.listdir(os.path.join(snap, 'domain')):
    m = name_re.match(f)
    if not m:
        continue
    d, fr, to, ext = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
    if ext == 'kv':
        kv.setdefault(d, []).append((fr, to))
    elif ext in ('kvi', 'bt'):
        acc.add((d, fr, to))
for d, rs in sorted(kv.items()):
    rs.sort(key=lambda r: (r[0], -r[1]))
    reach, gaps = 0, []
    for fr, to in rs:
        if fr > reach:
            gaps.append((reach, fr))
        reach = max(reach, to)
    no_acc = [r for r in rs if (d, *r) not in acc]
    report(not gaps and not no_acc, f'domain {d}', f'steps 0-{reach}, files {len(rs)}, gaps {gaps}, no accessor {no_acc}')

if a.stop_block is not None:
    tos = [int(m.group(2)) * 1000 for f in os.listdir(snap)
           if (m := re.match(r'^v[\d.]+-(\d+)-(\d+)-headers\.seg$', f))]
    top = max(tos, default=0)
    report(top > a.stop_block, 'header segments reach stop block', f'segments end at {top}, stop {a.stop_block}')

if a.bal_dir:
    idx = os.path.join(a.bal_dir, 'temp-bal.v1.idx')
    log = os.path.join(a.bal_dir, 'temp-bal.v1.log')
    if os.path.exists(idx) and os.path.exists(log):
        with open(idx, 'rb') as f:
            magic, first = f.read(8), struct.unpack('<Q', f.read(8))[0]
        last = first + (os.path.getsize(idx) - 16) // 8 - 1
        ok = magic == b'TMPBALI1' and (a.bal_from is None or first <= a.bal_from) and \
            (a.stop_block is None or last >= a.stop_block)
        report(ok, 'offline-BAL store covers range', f'{first}..{last}, need {a.bal_from}..{a.stop_block}')
    else:
        report(False, 'offline-BAL store present', f'{log} / {idx} missing')

if a.integration and a.expect_exec is not None:
    st = subprocess.run([a.integration, 'print_stages', f'--datadir={dd}'], capture_output=True, text=True).stdout
    m = re.search(r'^Execution\s+(\d+)', st, re.M)
    got = int(m.group(1)) if m else None
    report(got == a.expect_exec, 'print_stages Execution', f'{got}, expect {a.expect_exec}')

free = shutil.disk_usage(dd).free // 10**9
report(free >= a.min_free_gb, 'free NVMe space', f'{free} GB, need {a.min_free_gb} GB')

text = '\n'.join([f'precheck {dd} layout={a.layout} at {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}'] + out +
                 [f'RESULT {"FAIL" if fails else "OK"} ({fails} failed)'])
print(text)
os.makedirs(os.path.join(dd, 'logs'), exist_ok=True)
with open(os.path.join(dd, 'logs', time.strftime('precheck_%Y%m%dT%H%M%SZ.txt', time.gmtime())), 'w') as f:
    f.write(text + '\n')
sys.exit(1 if fails else 0)
