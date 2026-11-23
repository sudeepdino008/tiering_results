#!/bin/bash
# Stage 17 matrix driver: per cell (L, M) from order.txt: prepare, 10,000-block chaintip run, report, delete, push.
# usage: tv2_matrix.sh [L:M[:w2] ...]   (default: every cell of order.txt without a stats.json with rc 0)
# A cell with :w2 runs at W2 = 26,130,000 (base tv2_1s_base_w2, blocks 26,130,001..26,140,000).
# env MX (results folder; its name is the run-name suffix), COLDROOT (run cold dirs, e.g. /sbackup).
# Scripts run from frozen copies in $FROZEN; restart the driver to pick up script edits.
{
set -uo pipefail
MX=${MX:-/home/moskud/tiering_results/matrix_run/2026-11-16}
SRC=/erigon-data/tv2_scripts
FROZEN=/erigon-data/tv2_logs/stage17/scripts
BIN=/erigon-data/tv2_logs/stage16/bin
HDD=/backup/erigon-hdd
export COLDROOT=${COLDROOT:-$HDD} TV2_MX=$MX
NOTES=/home/moskud/worktrees/tiering_v2/ralph_notes.md
PY=$SRC/.venv/bin/python
declare -A HOT1=([6mo]=730 [4mo]=490 [3mo]=370 [1mo]=125 [6mow2]=730 [9mow2]=1080)
declare -A COLDNEW=([6mo]=6 [4mo]=45 [3mo]=68 [1mo]=110 [6mow2]=70 [9mow2]=45)
declare -A RATIO=([1]=0 [4]=0.70 [32]=0.36 [64]=0.30 [128]=0.25)

log() { echo "$(date -u +%FT%TZ) $*" | tee -a $MX/driver.log; }
free_gb() { df --output=avail -BG / | tail -1 | tr -dc 0-9; }
tpl_of() { [ "$2" = 1 ] && echo tv2_tpl_$1$3 || echo tv2_tpl_$1$3_h$2; }

delete() { # deletable per the stage-17 policy; every deletion is logged in ralph_notes.md
  local p
  for p in "$@"; do
    [ -e "$p" ] || continue
    case $p in /erigon-data/tv2_mx_*|/erigon-data/tv2_tpl_*|/erigon-data/*_coldstage|$HDD/tv2_mx_*|$HDD/tv2_tpl_*|/sbackup/tv2_mx_*) ;;
      *) log "refusing to delete $p"; return 1 ;; esac
    rm -rf "$p" && echo "- $(date -u +%FT%TZ) stage 17 driver deleted $p" >> $NOTES
  done
}

push() {
  git -C $MX/../.. add matrix_run scripts && git -C $MX/../.. commit -qm "matrix_run: $1" && git -C $MX/../.. push -q || log "push failed ($1)"
}

done_cell() { [ -f $1/stats.json ] && $PY -c "import json,sys; sys.exit(json.load(open('$1/stats.json'))['rc'] != 0)"; }

cell() { # returns 0 = done/ran, 2 = skipped: space
  local L=$1 M=$2 V=${3:-} W=25400000 BASE=/erigon-data/tv2_1s_base SFX=
  [ "$V" = w2 ] && { W=26130000; BASE=/erigon-data/tv2_1s_base_w2; SFX=_w2; }
  local C=$MX/cells/${L}_m$M$SFX NAME=tv2_mx_${L}_m$M$SFX RUN=mx_${L}_m${M}_w${W}_$(basename $MX)
  local DD=/erigon-data/$NAME TPL; TPL=$(tpl_of $L $M $SFX)
  done_cell $C && return 0
  local est=15
  [ -f /erigon-data/$TPL/TPL_BOUNDARY ] || est=$(echo "${COLDNEW[$L$V]} + ${HOT1[$L$V]} * ${RATIO[$M]} + 15" | bc | cut -d. -f1)
  if [ $((est + 60)) -gt $(free_gb) ]; then
    log "cell $L/$M$SFX skipped: space (est $est GB + 60 > free $(free_gb) GB)"
    return 2
  fi
  mkdir -p $C/logs; rm -f $C/stats.json
  echo "$L $M $V" > $MX/running.txt
  $PY $FROZEN/tv2_matrix_report.py report > /dev/null && push "start $L/$M"
  [ -f /erigon-data/$TPL/TPL_BOUNDARY ] || delete /erigon-data/$TPL /erigon-data/${TPL}_coldstage $HDD/$TPL
  delete $DD $COLDROOT/$NAME
  log "cell $L/$M$SFX: prepare (est new $est GB, free $(free_gb) GB)"
  local t0=$SECONDS rc
  W=$W BASE=$BASE TAG=$SFX ERIGON=$BIN/erigon INTEGRATION=$BIN/integration bash $FROZEN/tv2_prepare.sh --lookback-blocks $L --hot-merge-steps $M --name $NAME > $C/logs/prepare.log 2>&1
  rc=$?
  if [ $rc = 0 ]; then
    log "cell $L/$M$SFX: prepared in $((SECONDS - t0)) s; run $RUN"
    $PY $FROZEN/tv2_matrix_report.py layout $DD > $C/layout_before.md
    MODE=chaintip STOP=$((W + 10000)) BALFROM=$((W + 1)) BIN=$BIN STAGE=17 EXTRA=--tiering.cold-io-max-mbps=50 \
      bash $FROZEN/tv2_demote_run.sh $DD $RUN > $C/logs/run_driver.log 2>&1
    rc=$(sed -nE 's/^done rc=([0-9]+)$/\1/p' $C/logs/run_driver.log); rc=${rc:-1}
    grep -q '^cgroup .*memory.max 68719476736' $DD/logs/memcg.txt || { log "cell $L/$M$SFX: memory.max is not 64G"; [ "$rc" = 0 ] && rc=99; }
    python3 $FROZEN/precheck.py --layout tiered --cold-dir $COLDROOT/$NAME/domain $DD > $C/logs/precheck_after.txt 2>&1 \
      || log "cell $L/$M$SFX: post-run precheck FAIL"
    cp $DD/logs/precheck_*.txt $DD/logs/memcg.txt $DD/logs/demote.csv $C/logs/ 2>/dev/null
    tail -300 $DD/logs/run.out > $C/logs/run_tail.out
    $PY $FROZEN/tv2_matrix_report.py stats $C $RUN $DD $L $M $rc $W > $C/logs/stats.out 2>&1
    python3 $FROZEN/tv2_report.py $RUN --out $MX/cells --name ${L}_m$M$SFX > $C/logs/report.out 2>&1 || log "cell $L/$M$SFX: tv2_report failed"
  else
    log "cell $L/$M$SFX: prepare failed rc=$rc"
    echo "{\"run\": \"$RUN\", \"L\": \"$L\", \"M\": $M, \"rc\": $rc, \"error_excerpt\": \"prepare failed, see logs/prepare.log\"}" > $C/stats.json
  fi
  log "cell $L/$M$SFX: rc=$rc in $(( (SECONDS - t0) / 60 )) min; $(grep -oE '"mgas_s_per_block": [0-9.]+' $C/stats.json)"
  rm -f $MX/running.txt
  delete $DD $COLDROOT/$NAME /erigon-data/$TPL $HDD/$TPL
  $PY $FROZEN/tv2_matrix_report.py report > /dev/null
  push "cell $L/$M$SFX rc=$rc"
  return 0
}

main() {
  mkdir -p $FROZEN
  cp $SRC/{tv2_prepare.sh,tv2_demote_run.sh,tv2_report.py,tv2_matrix_report.py,precheck.py,tv2_matrix.sh} $FROZEN/
  cp $SRC/{tv2_prepare.sh,tv2_demote_run.sh,tv2_report.py,tv2_matrix_report.py,precheck.py,tv2_matrix.sh} $MX/../../scripts/
  local cells=("$@") todo skipped
  [ ${#cells[@]} -gt 0 ] || mapfile -t cells < <(awk '/^[0-9]/{print $3":"$4($6 ? ":"$6 : "")}' $MX/order.txt)
  log "driver start: ${cells[*]}"
  todo=("${cells[@]}")
  while [ ${#todo[@]} -gt 0 ]; do
    skipped=()
    local ran=0 c cl cm cv
    for c in "${todo[@]}"; do
      IFS=: read -r cl cm cv <<< "$c"
      cell $cl $cm $cv
      case $? in 2) skipped+=($c) ;; *) ran=1 ;; esac
    done
    [ $ran = 1 ] || { log "only skipped cells left: ${skipped[*]}"; break; }
    todo=("${skipped[@]}")
  done
  log "driver end"
}

main "$@"
exit
}
