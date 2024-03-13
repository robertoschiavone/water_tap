#!/usr/bin/env bash
set -euo pipefail

total_time=0

for i in {1..1000}; do
    start=$(gdate +%s%N)
    python $1 > /dev/null
    end=$(gdate +%s%N)
    execution_time=$((end-start))
    total_time=$((total_time + execution_time))
done

average_time=$((total_time / 1000))
echo "Average execution time for $1: $average_time nanoseconds" >> profile.txt
