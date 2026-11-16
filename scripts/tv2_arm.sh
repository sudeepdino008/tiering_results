#!/bin/bash
# usage: tv2_arm.sh <name> <bal 0|1> — one stage-14.1.a arm: fresh mirror of tv2_bl_base, chaintip W..W+5000, pprof.
set -uo pipefail
NAME=$1; BAL=$2
WT=/home/moskud/worktrees/tiering_v2; BASE=/erigon-data/tv2_bl_base; DD=/erigon-data/tv2_bl_$NAME
C=037cfbb98b; W=25400000; STOP=25405000; MPORT=6077; PPORT=6061; RUN=bl141a_$NAME
[ -d $DD ] && rm -rf $DD
bash $WT/cmd/scripts/mirror-datadir.sh $BASE $DD | tail -1
mkdir -p $DD/logs/pprof
O=$DD/logs/precheck_$(date -u +%Y%m%dT%H%M%SZ).txt
python3 /erigon-data/tv2_scripts/precheck.py --layout ssd --stop-block $STOP --bal-dir /erigon-data/offline-bal-8192-tip --bal-from $((W+1)) --integration $WT/build/bin/integration --expect-exec $W --min-free-gb 100 $DD > $O 2>&1 || { echo "precheck FAIL $O"; exit 1; }
FLAGS="--prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 --exec.state-cache=false --pfb.sync.mode.chaintip --pfb.exec.stop-at-block=$STOP --metrics --metrics.addr=127.0.0.1 --metrics.port=$MPORT --pprof --pprof.port=$PPORT"
[ "$BAL" = 1 ] && FLAGS="$FLAGS --use-offline-bals --offline-bal.dir=/erigon-data/offline-bal-8192-tip"
python3 /erigon-data/tv2_scripts/tv2_register.py $MPORT $RUN baseline $DD $C
{ echo "== free before drop"; free -h; sync; sudo -n sh -c 'echo 3 > /proc/sys/vm/drop_caches'; echo "== free after global drop"; free -h; } >> $O
OUT=$DD/logs/arm.out
/erigon-data/tv2_scripts/tv2_mark.sh "start $RUN" run=$RUN stage=14.1 event=start datadir=$DD "flags=$FLAGS"
echo "start $(date -u +%FT%TZ) commit $C" > $OUT
systemd-run --user --scope -q -p MemoryMax=64G -p MemorySwapMax=0 $BASE/bin/erigon-$C --datadir=$DD --chain=mainnet $FLAGS --log.dir.path=$DD/logs >> $OUT 2>&1 &
PID=$!
prof() { # $1 = block to wait for, $2 = tag
  until grep -a 'Execution\].*committed' $OUT | tail -1 | grep -oE 'blk=[0-9]+' | awk -F= -v b=$1 '$2>=b{f=1} END{exit !f}'; do
    kill -0 $PID 2>/dev/null || return; sleep 5; done
  go tool pprof -proto "http://127.0.0.1:$PPORT/debug/pprof/profile?seconds=30" > $DD/logs/pprof/cpu_$2.pb.gz 2>/dev/null
  echo "cpu profile $2 at $(date -u +%T)"
}
prof $((W+1000)) 1
prof $((W+2500)) 2
curl -s "http://127.0.0.1:$PPORT/debug/pprof/heap" > $DD/logs/pprof/heap.pb.gz && echo "heap profile"
prof $((W+4000)) 3
wait $PID; rc=$?
echo "exit rc=$rc $(date -u +%FT%TZ)" >> $OUT
/erigon-data/tv2_scripts/tv2_mark.sh "stop $RUN rc=$rc" run=$RUN stage=14.1 event=stop datadir=$DD
echo "done $NAME rc=$rc"
