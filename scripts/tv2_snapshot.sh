#!/bin/bash
# usage: tv2_snapshot.sh <name>   -> /backup/tv2_metrics/<name>/ (hardlinks unchanged blocks from the previous backup)
set -e
name=$1; [ -n "$name" ] || { echo "usage: $0 <name>"; exit 1; }
M=/erigon-data/tv2_metrics; B=/backup/tv2_metrics; mkdir -p $B
snap=$(curl -sf -X POST http://127.0.0.1:9091/api/v1/admin/tsdb/snapshot | python3 -c "import json,sys; print(json.load(sys.stdin)['data']['name'])")
prev=$(ls -1dt $B/*/ 2>/dev/null | head -1)
rsync -a ${prev:+--link-dest=$prev} $M/prometheus/snapshots/$snap/ $B/$name/
cp $M/marks.jsonl $M/targets.json $B/$name/
rm -rf $M/prometheus/snapshots/$snap
du -sh $B/$name
