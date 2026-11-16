#!/bin/bash
# Stage 14.1 baseline: fresh mirror of tv2_bl_base, chaintip from W with offline BALs, samplers + marks.
set -uo pipefail
WT=/home/moskud/worktrees/tiering_v2; BASE=/erigon-data/tv2_bl_base; DD=/erigon-data/tv2_bl_run
C=57539c60f9; W=25400000; MPORT=6078; NOMETRICS=${NOMETRICS:-0}
# BLOCKS=N: stop by itself at W+N (measured run); MINUTES=M: SIGINT after M minutes (quick run)
BLOCKS=${BLOCKS:-10000}; MINUTES=${MINUTES:-0}
CAP=$((W+BLOCKS)); [ "$MINUTES" -gt 0 ] && CAP=25420000
RUN=${RUN:-baseline_allssd_merged_6mo_w25400000_2026-10-23-3}; [ "$NOMETRICS" = 1 ] && RUN=${RUN}_nometrics
[ -d $DD ] && { echo "$DD exists, remove it first"; exit 1; }
bash $WT/cmd/scripts/mirror-datadir.sh $BASE $DD | tail -1
O=$DD/logs/precheck_$(date -u +%Y%m%dT%H%M%SZ).txt
python3 /erigon-data/tv2_scripts/precheck.py --layout ssd --stop-block $CAP --bal-dir /erigon-data/offline-bal-8192-tip --bal-from $((W+1)) --integration $WT/build/bin/integration --expect-exec $W --min-free-gb 100 $DD > $O 2>&1 || { echo "precheck FAIL $O"; exit 1; }
FLAGS="--prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=true --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip --pfb.sync.mode.chaintip --pfb.exec.stop-at-block=$CAP --tiering.lookback-blocks=1296000 --metrics --metrics.addr=127.0.0.1 --metrics.port=$MPORT"
KVRM=true
[ "$NOMETRICS" = 1 ] && { FLAGS=${FLAGS% --tiering.lookback-blocks=*}; KVRM=false; }
IOS=
if [ "$NOMETRICS" != 1 ]; then
  python3 /erigon-data/tv2_scripts/tv2_register.py $MPORT $RUN baseline $DD $C
  iostat -x -t nvme0n1 sda 1 > $DD/logs/iostat.txt 2>&1 & IOS=$!
fi
{ echo "== free before drop"; free -h; sync; sudo -n sh -c 'echo 3 > /proc/sys/vm/drop_caches'; echo "== free after global drop"; free -h; } >> $O
OUT=$DD/logs/baseline.out
/erigon-data/tv2_scripts/tv2_mark.sh "start $RUN" run=$RUN stage=14.1 event=start datadir=$DD "flags=KV_READ_METRICS=$KVRM $FLAGS"
echo "start $(date -u +%FT%TZ) commit $C" > $OUT
KV_READ_METRICS=$KVRM systemd-run --user --scope -q -p MemoryMax=64G -p MemorySwapMax=0 $BASE/bin/erigon-$C --datadir=$DD --chain=mainnet $FLAGS --log.dir.path=$DD/logs >> $OUT 2>&1 &
PID=$!
[ "$NOMETRICS" != 1 ] && ( while kill -0 $PID 2>/dev/null; do echo "$(date +%s) $(awk '{print $12, $10}' /proc/$PID/stat 2>/dev/null)"; sleep 1; done ) > $DD/logs/faults.txt &
if [ "$MINUTES" -gt 0 ]; then
  END=$(( $(date +%s) + MINUTES*60 ))
  while kill -0 $PID 2>/dev/null && [ $(date +%s) -lt $END ]; do sleep 5; done
  kill -INT $PID 2>/dev/null
fi
wait $PID; rc=$?
[ -n "$IOS" ] && kill $IOS 2>/dev/null
echo "exit rc=$rc $(date -u +%FT%TZ)" >> $OUT
/erigon-data/tv2_scripts/tv2_mark.sh "stop $RUN rc=$rc" run=$RUN stage=14.1 event=stop datadir=$DD
echo "last block: $(grep -a 'parallel committed' $OUT | tail -1 | grep -oE 'blk=[0-9]+')"
echo "done rc=$rc"
