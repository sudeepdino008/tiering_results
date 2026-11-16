#!/bin/bash
cd /home/moskud/worktrees/tiering_v2
for a in "arm2a 0" "arm2b 0" "arm3 1"; do /erigon-data/tv2_scripts/tv2_arm.sh $a; done
echo "all arms done $(date -u +%FT%TZ)"
