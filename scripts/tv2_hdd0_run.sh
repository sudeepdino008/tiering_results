#!/bin/bash
# Stage 15 run A: v1 layout (only commitment 0-8192 on HDD, no demotion), chaintip from W for BLOCKS blocks.
# usage: tv2_hdd0_run.sh <base datadir> <run datadir> <run name> [extra erigon flags...]
# env COLD=<dir on HDD>: 0-8192 is hardlinked into COLD and demotion runs with --tiering.cold-dir=COLD; LB = lookback blocks
set -uo pipefail
BASE=$1; DD=$2; RUN=$3; shift 3; EXTRA="$*"
WT=/home/moskud/worktrees/tiering_v2; BIN=/erigon-data/tv2_logs/stage15/bin
W=25400000; BLOCKS=${BLOCKS:-2000}; MPORT=${MPORT:-6081}; STOP=$((W+BLOCKS)); LB=${LB:-1296000}; COLD=${COLD:-}
HDD0=/backup/erigon-hdd/domain/v2.2-commitment.0-8192.kv
C=$($BIN/erigon --version | tail -1 | grep -oE '[0-9a-f]{8,}$' | cut -c1-10)
[ -e $DD ] && { echo "$DD exists"; exit 1; }
bash $WT/cmd/scripts/mirror-datadir.sh $BASE $DD | tail -1
rm -rf $DD/logs; mkdir $DD/logs
K=$DD/snapshots/domain/v2.2-commitment.0-8192.kv
[ "$(stat -c %s $K)" = "$(stat -c %s $HDD0)" ] || { echo "0-8192 size differs from $HDD0"; exit 1; }
LAYOUT="--layout hdd0"
if [ -n "$COLD" ]; then
  [ -e $COLD ] && { echo "$COLD exists"; exit 1; }
  mkdir -p $COLD && ln $HDD0 $COLD/
  TX=$($BIN/erigon snapshots txnum --datadir=$DD --block=$((W-LB)) 2>&1 | grep -oE 'min_txnum=[0-9]+' | cut -d= -f2)
  [ -n "$TX" ] || { echo "txnum lookup failed"; exit 1; }
  LAYOUT="--layout tiered --cold-dir $COLD --boundary-step $((TX/390625))"
  EXTRA="--tiering.cold-dir=$COLD --tiering.demote $EXTRA"
  HDD0=$COLD/$(basename $HDD0)
fi
rm -f $K; ln -s $HDD0 $K
O=$DD/logs/precheck_$(date -u +%Y%m%dT%H%M%SZ).txt
python3 /erigon-data/tv2_scripts/precheck.py $LAYOUT --stop-block $STOP --bal-dir /erigon-data/offline-bal-8192-tip --bal-from $((W+1)) \
  --integration $BIN/integration --expect-exec $W --min-free-gb 100 $DD > $O 2>&1 || { echo "precheck FAIL $O"; exit 1; }
FLAGS="--prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.sync.mode.chaintip --pfb.exec.stop-at-block=$STOP --tiering.lookback-blocks=$LB --metrics --metrics.addr=127.0.0.1 --metrics.port=$MPORT $EXTRA"
python3 /erigon-data/tv2_scripts/tv2_register.py $MPORT $RUN baseline $DD $C
iostat -x -t nvme0n1 sda 1 > $DD/logs/iostat.txt 2>&1 & IOS=$!
{ echo "== free before drop"; free -h; sync; sudo -n sh -c 'echo 3 > /proc/sys/vm/drop_caches'; echo "== free after global drop"; free -h; } >> $O
OUT=$DD/logs/run.out
/erigon-data/tv2_scripts/tv2_mark.sh "start $RUN" run=$RUN stage=15 event=start datadir=$DD "flags=KV_READ_METRICS=true $FLAGS"
echo "start $(date -u +%FT%TZ) commit $C" > $OUT
KV_READ_METRICS=true systemd-run --user --scope -q -p MemoryMax=64G -p MemorySwapMax=0 $BIN/erigon --datadir=$DD --chain=mainnet $FLAGS --log.dir.path=$DD/logs >> $OUT 2>&1 &
PID=$!
( while kill -0 $PID 2>/dev/null; do echo "$(date +%s) $(awk '{print $12, $10}' /proc/$PID/stat 2>/dev/null)"; sleep 1; done ) > $DD/logs/faults.txt &
wait $PID; rc=$?
kill $IOS 2>/dev/null
echo "exit rc=$rc $(date -u +%FT%TZ)" >> $OUT
/erigon-data/tv2_scripts/tv2_mark.sh "stop $RUN rc=$rc" run=$RUN stage=15 event=stop datadir=$DD
python3 - $MPORT <<'EOF'
import json, sys
p = '/erigon-data/tv2_metrics/targets.json'
t = [x for x in json.load(open(p)) if x['targets'] != ['127.0.0.1:' + sys.argv[1]]]
json.dump(t, open(p, 'w'), indent=1)
EOF
echo "last block: $(grep -a 'parallel committed\|parallel done' $OUT | tail -1 | grep -oE 'blk=[0-9]+')"
echo "done rc=$rc"
