set -e

cut comparison_check.csv -d ',' -f 3,4,5,6,7 | sort | uniq -c | sort -n