#!/bin/bash
# Stage 15 demotion run on a datadir made by tv2_prepare.sh: precheck tiered, cache drop, marks, iostat + faults + demote samplers.
# usage: tv2_demote_run.sh <datadir> <run name>; env MODE=batch|chaintip, STOP=<block>, MINUTES=<SIGINT after M min, 0 = off>
set -uo pipefail
DD=$1; RUN=$2
MODE=${MODE:-batch}; STOP=${STOP:-25420000}; MINUTES=${MINUTES:-0}; MPORT=${MPORT:-6080}
BIN=/erigon-data/tv2_logs/stage15/bin; C=$($BIN/erigon --version | tail -1 | grep -oE '[0-9a-f]{8,}$' | cut -c1-10)
read -r LB COLD < <(sed -nE 's/.*--tiering.cold-dir=([^ ]+) --tiering.lookback-blocks=([0-9]+).*/\2 \1/p' $DD/TV2_README.md)
BSTEP=$(sed -nE 's/.*cold boundary: block [0-9]+, min_txnum [0-9]+, step ([0-9]+).*/\1/p' $DD/TV2_README.md)
[ -n "$LB" ] && [ -n "$COLD" ] && [ -n "$BSTEP" ] || { echo "cannot read L/cold dir/boundary from $DD/TV2_README.md"; exit 1; }
O=$DD/logs/precheck_$(date -u +%Y%m%dT%H%M%SZ).txt
python3 /erigon-data/tv2_scripts/precheck.py --layout tiered --cold-dir $COLD --boundary-step $BSTEP --stop-block $STOP \
  --bal-dir /erigon-data/offline-bal-8192-tip --bal-from 25400001 --integration $BIN/integration --min-free-gb 100 $DD > $O 2>&1 \
  || { echo "precheck FAIL $O"; exit 1; }
FLAGS="--prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.exec.stop-at-block=$STOP --tiering.commitment-hot-merge-steps=1 --tiering.lookback-blocks=$LB --tiering.cold-dir=$COLD --tiering.demote --metrics --metrics.addr=127.0.0.1 --metrics.port=$MPORT"
[ "$MODE" = chaintip ] && FLAGS="$FLAGS --pfb.sync.mode.chaintip"
python3 /erigon-data/tv2_scripts/tv2_register.py $MPORT $RUN demotion $DD $C
iostat -x -t nvme0n1 sda 1 > $DD/logs/iostat.txt 2>&1 & IOS=$!
{ echo "== free before drop"; free -h; sync; sudo -n sh -c 'echo 3 > /proc/sys/vm/drop_caches'; echo "== free after global drop"; free -h; } >> $O
OUT=$DD/logs/run.out
/erigon-data/tv2_scripts/tv2_mark.sh "start $RUN" run=$RUN stage=15 event=start datadir=$DD "flags=KV_READ_METRICS=true $FLAGS"
echo "start $(date -u +%FT%TZ) commit $C mode $MODE" > $OUT
KV_READ_METRICS=true $BIN/erigon --datadir=$DD --chain=mainnet $FLAGS --log.dir.path=$DD/logs >> $OUT 2>&1 &
PID=$!
( while kill -0 $PID 2>/dev/null; do echo "$(date +%s) $(awk '{print $12, $10}' /proc/$PID/stat 2>/dev/null)"; sleep 1; done ) > $DD/logs/faults.txt &
python3 /erigon-data/tv2_scripts/demote_sampler.py $DD $COLD $OUT $DD/logs/demote.csv 30 > /dev/null 2>&1 & SMP=$!
if [ "$MINUTES" -gt 0 ]; then
  END=$(( $(date +%s) + MINUTES*60 ))
  while kill -0 $PID 2>/dev/null && [ $(date +%s) -lt $END ]; do sleep 5; done
  kill -INT $PID 2>/dev/null
fi
wait $PID; rc=$?
kill $IOS $SMP 2>/dev/null
echo "exit rc=$rc $(date -u +%FT%TZ)" >> $OUT
/erigon-data/tv2_scripts/tv2_mark.sh "stop $RUN rc=$rc" run=$RUN stage=15 event=stop datadir=$DD
echo "last block: $(grep -a 'parallel committed\|\[4/6 Execution\] .*blk=' $OUT | tail -1 | grep -oE 'blk=[0-9]+')"
echo "done rc=$rc"
