set -e

cut mine/tod_candidates_evaluation.csv -d ',' -f 3 | sort | uniq -c | sort -n