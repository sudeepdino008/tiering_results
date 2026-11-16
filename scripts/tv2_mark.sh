#!/bin/bash
# usage: tv2_mark.sh "<text>" [k=v ...]   (common keys: run=, stage=, event=start|stop|precheck|reset|demote, datadir=, flags=)
exec python3 -I - "$@" <<'PY'
import json, os, sys, time, urllib.request
M = '/erigon-data/tv2_metrics'
text, tags = sys.argv[1], dict(a.split('=', 1) for a in sys.argv[2:])
ts = time.time()
with open(f'{M}/marks.jsonl', 'a') as f:
    f.write(json.dumps({'ts': ts, 'text': text, **tags}) + '\n')
esc = lambda v: v.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
lines = []
for l in open(f'{M}/marks.jsonl'):
    m = json.loads(l)
    t = m.pop('ts')
    m.pop('flags', None)
    lbl = ','.join(f'{k}="{esc(str(v))}"' for k, v in sorted(m.items()))
    lines.append(f'tv2_mark{{{lbl}}} {t:.3f}')
tmp = f'{M}/textfile/tv2_marks.prom.tmp'
with open(tmp, 'w') as f:
    f.write('# TYPE tv2_mark gauge\n' + '\n'.join(lines) + '\n')
os.replace(tmp, f'{M}/textfile/tv2_marks.prom')
try:
    tok = open(f'{M}/grafana_token').read().strip()
    req = urllib.request.Request('http://127.0.0.1:3000/api/annotations', method='POST',
        data=json.dumps({'time': int(ts * 1000), 'text': text, 'tags': [f'{k}:{v}' for k, v in tags.items() if k != 'flags']}).encode(),
        headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {tok}'})
    urllib.request.urlopen(req, timeout=3)
except OSError:
    pass
print(f'mark {ts:.0f} {text} {tags}')
PY
