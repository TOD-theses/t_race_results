set -e

cut comparison_duplicate_limit.csv -d ',' -f 3,4,5,6,7,8 | sort | uniq -c | sort -n