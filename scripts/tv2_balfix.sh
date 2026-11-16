#!/bin/bash
# usage: tv2_balfix.sh <datadir at a block below N> <N>
# Regenerates the offline BALs from the datadir's Execution+1 to N with the fixed generator (no BAL use)
# on a scratch mirror and patches them into the store in place.
set -euo pipefail
SRC=$1; N=$2
WT=/home/moskud/worktrees/tiering_v2
STORE=/erigon-data/offline-bal-8192-tip
TMP=/erigon-data/tv2_balfix_tmp
BIN=$(ls -t $SRC/bin/erigon-* | head -1)
PATCHBIN=$(ls -t /erigon-data/tv2_scripts/offlinebal-patch-* | head -1)
LOG=/erigon-data/tv2_logs/balfix_$N.out
exec > >(tee -a $LOG) 2>&1
echo "start $(date -u +%FT%TZ) src=$SRC N=$N bin=$BIN"
[ -d $TMP ] && rm -rf $TMP
bash $WT/cmd/scripts/mirror-datadir.sh $SRC $TMP | tail -1
E=$($WT/build/bin/integration print_stages --datadir=$TMP 2>&1 | awk '/^Execution/{print $2}')
echo "exec=$E"
python3 /erigon-data/tv2_scripts/precheck.py --layout ssd --stop-block $N --integration $WT/build/bin/integration --expect-exec $E --min-free-gb 100 $TMP | grep RESULT
free -h; sync; sudo -n sh -c 'echo 3 > /proc/sys/vm/drop_caches'; free -h
$BIN --datadir=$TMP --chain=mainnet --prune.mode=full --prune.distance.blocks=10000000 --externalcl --no-downloader --maxpeers=0 \
  --generate-offline-bals --offline-bal.dir=$TMP/balpatch --exec.state-cache=false --pfb.exec.stop-at-block=$N \
  --log.dir.path=$TMP/logs > $TMP/gen.out 2>&1 || true
grep -a 'Wrong trie root' $TMP/gen.out && { echo "BAL-less run failed"; exit 1; }
python3 /erigon-data/tv2_logs/balwalk.py $TMP/balpatch/temp-bal.v1.log
$PATCHBIN -in-place -src $STORE -patch $TMP/balpatch
rm -rf $TMP
echo "end $(date -u +%FT%TZ)"
