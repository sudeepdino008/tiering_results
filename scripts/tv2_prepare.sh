#!/bin/bash
# Prepares a run datadir at W for one lookback: commitment files fully older than W - L are cold (HDD, pre-merged).
# usage: tv2_prepare.sh --lookback-blocks <1mo|3mo|6mo|N> [--name <datadir name>]
# Per L a template (tv2_tpl_<L> + /backup/erigon-hdd/tv2_tpl_<L>/domain) is built once; a run is a hardlink copy of it.
# 1-step cold copies are shared through the pool /backup/erigon-hdd/pool_1s_W (one HDD copy per file name).
set -euo pipefail
W=25400000
BASE=/erigon-data/tv2_1s_base
HDD=/backup/erigon-hdd
POOL=$HDD/pool_1s_W
SHARED0=$HDD/domain/v2.2-commitment.0-8192.kv
SIZE0=180470634040
STEP=390625
WT=/home/moskud/worktrees/tiering_v2
ERIGON=${ERIGON:-$WT/build/bin/erigon}
INTEGRATION=${INTEGRATION:-$WT/build/bin/integration}
MIRROR=$WT/cmd/scripts/mirror-datadir.sh

L=""; NAME=""
while [ $# -gt 0 ]; do
  case $1 in
    --lookback-blocks) L=$2; shift 2 ;;
    --name) NAME=$2; shift 2 ;;
    *) echo "unknown arg $1"; exit 2 ;;
  esac
done
case $L in
  1mo) LB=216000 ;; 3mo) LB=648000 ;; 6mo) LB=1296000 ;;
  ''|*[!0-9]*) echo "--lookback-blocks: 1mo|3mo|6mo|<blocks>"; exit 2 ;;
  *) LB=$L; L=${L}b ;;
esac
NAME=${NAME:-tv2_run_$L}
TPL=tv2_tpl_$L
log() { echo "$(date -u +%FT%TZ) $*"; }

exec_progress() { $INTEGRATION print_stages --datadir=$1 2>&1 | awk '/^Execution/{print $2}'; }

relink_cold() { # point every commitment symlink of datadir $1 at a hardlink in cold dir $2
  local dd=$1 cold=$2 l t
  mkdir -p $cold
  for l in $(find $dd/snapshots/domain -maxdepth 1 -type l); do
    t=$(readlink $l)
    [ "$(dirname $t)" = "$cold" ] && continue
    ln $t $cold/
    ln -sfn $cold/$(basename $l) $l
  done
}

build_template() {
  local dd=/erigon-data/$TPL cold=$HDD/$TPL/domain t0=$SECONDS
  [ -e $dd ] || [ -e $HDD/$TPL ] && { echo "partial template $dd or $HDD/$TPL exists; remove it first"; exit 1; }
  log "template $TPL: mirror $BASE"
  $MIRROR $BASE $dd > /dev/null
  rm -rf $dd/logs; mkdir $dd/logs
  local e; e=$(exec_progress $dd)
  [ "$e" = "$W" ] || { echo "Execution=$e, want $W"; exit 1; }
  local b=$((W - LB)) tx
  tx=$($ERIGON snapshots txnum --datadir=$dd --block=$b 2>&1 | grep -oE 'min_txnum=[0-9]+' | cut -d= -f2)
  [ -n "$tx" ] || { echo "txnum lookup failed for block $b"; exit 1; }
  local bstep=$((tx / STEP))
  log "boundary block $b min_txnum $tx step $bstep"
  mkdir -p $cold $POOL
  [ "$(stat -c %s $SHARED0)" = "$SIZE0" ] || { echo "bad size $SHARED0"; exit 1; }
  [ -e $POOL/$(basename $SHARED0) ] || ln $SHARED0 $POOL/
  local f n to s ncold=0
  for f in $dd/snapshots/domain/v*-commitment.*.kv; do
    n=$(basename $f)
    to=$(echo $n | sed -E 's/.*\.[0-9]+-([0-9]+)\.kv$/\1/')
    [ $((to * STEP)) -le $tx ] || continue
    s=$(stat -c %s $f)
    if [ ! -e $POOL/$n ]; then
      cp $f $POOL/$n.tmp
      [ "$(stat -c %s $POOL/$n.tmp)" = "$s" ] || { echo "copy size mismatch $n"; exit 1; }
      mv $POOL/$n.tmp $POOL/$n
    fi
    [ "$(stat -c %s $POOL/$n)" = "$s" ] || { echo "pool size mismatch $n"; exit 1; }
    ln $POOL/$n $cold/$n
    rm -f $f
    ln -s $cold/$n $f
    ncold=$((ncold + 1))
  done
  log "cold files linked: $ncold (below step $bstep) in $((SECONDS - t0)) s"
  log "tiered seg retire"
  $ERIGON snapshots retire --datadir=$dd --tiering.cold-dir=$cold --tiering.commitment-hot-merge-steps=1 > $dd/logs/retire_tiered.out 2>&1 \
    || { echo "retire failed: $dd/logs/retire_tiered.out"; exit 1; }
  e=$(exec_progress $dd)
  [ "$e" = "$W" ] || { echo "after retire Execution=$e, want $W"; exit 1; }
  python3 /erigon-data/tv2_scripts/precheck.py --layout tiered --cold-dir $cold --boundary-step $bstep $dd > $dd/logs/precheck_tpl.txt 2>&1 \
    || { echo "template precheck FAIL: $dd/logs/precheck_tpl.txt"; exit 1; }
  echo "$b $tx $bstep" > $dd/TPL_BOUNDARY
  log "template done in $((SECONDS - t0)) s"
}

[ -e /erigon-data/$NAME ] && { echo "/erigon-data/$NAME exists"; exit 1; }
[ -e $HDD/$NAME ] && { echo "$HDD/$NAME exists"; exit 1; }
[ -f /erigon-data/$TPL/TPL_BOUNDARY ] || build_template
read B TX BSTEP < /erigon-data/$TPL/TPL_BOUNDARY

T0=$SECONDS
DD=/erigon-data/$NAME; COLD=$HDD/$NAME/domain
log "run $NAME: mirror $TPL"
$MIRROR /erigon-data/$TPL $DD > /dev/null
rm -rf $DD/logs $DD/TPL_BOUNDARY; mkdir $DD/logs
relink_cold $DD $COLD
O=$DD/logs/precheck_prep_$(date -u +%Y%m%dT%H%M%SZ).txt
python3 /erigon-data/tv2_scripts/precheck.py --layout tiered --cold-dir $COLD --boundary-step $BSTEP --integration $INTEGRATION --expect-exec $W $DD > $O 2>&1 \
  || { echo "precheck FAIL: $O"; exit 1; }
NC=$(ls $COLD | wc -l)
BC=$(du -bc $COLD/* | tail -1 | cut -f1)
NH=$(ls $DD/snapshots/domain | grep -c 'commitment.*\.kv$')
cat > $DD/TV2_README.md <<EOF
# $NAME

Prepared by tv2_prepare.sh at $(date -u +%FT%TZ) from template $TPL (base $BASE).
- W = $W (Execution), lookback L = $LB blocks ($L)
- cold boundary: block $B, min_txnum $TX, step $BSTEP; commitment files ending at or below it are cold
- cold dir: $COLD ($NC files, $BC bytes, hardlinks of $HDD/$TPL/domain and the pool $POOL)
- commitment .kv files in snapshots/domain (symlinks included): $NH; hot 1-step files on SSD above the boundary
- run flags: --tiering.cold-dir=$COLD --tiering.lookback-blocks=$LB --tiering.commitment-hot-merge-steps=1 --tiering.demote
EOF
log "run $NAME ready in $((SECONDS - T0)) s: $NC cold files, $BC bytes; precheck $O"
