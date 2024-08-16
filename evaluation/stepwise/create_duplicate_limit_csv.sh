set -e

echo "tx_a,tx_b" > covered.csv
grep 'True' mine-duplicate-limit/tod_candidates_evaluation.csv | cut -d ',' -f 1,2 >> covered.csv

echo "tx_a,tx_b" > covered_by_single_tx.csv
grep 'True' mine-duplicate-limit/tod_candidates_evaluation.csv | grep -v '|' | cut -d ',' -f 1,2 >> covered_by_single_tx.csv

echo "tx_a,tx_b" > covered_partially.csv
grep 'False,0x' mine-duplicate-limit/tod_candidates_evaluation.csv | cut -d ',' -f 1,2 >> covered_partially.csv

echo "tx_a,tx_b" > not_covered.csv
grep 'False' mine-duplicate-limit/tod_candidates_evaluation.csv | cut -d ',' -f 1,2 >> not_covered.csv

echo "tx_a,tx_b" > removed_by_limit.csv
grep -E 'limited' mine/tod_candidates_evaluation.csv | cut -d ',' -f 1,2 >> removed_by_limit.csv


python3 compare_tods.py ../rq1-3_search.csv removed_by_limit.csv covered.csv covered_by_single_tx.csv covered_partially.csv not_covered.csv > comparison_duplicate_limit.csv