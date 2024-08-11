set -e

cut comparison.csv -d ',' -f 3,4,5,6 | sort | uniq -c | sort -n