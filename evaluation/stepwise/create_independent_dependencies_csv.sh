set -e

echo "tx_a,tx_b" > filtered_by_same_value_collision.csv
grep -E 'same-value collision' mine/tod_candidates_evaluation.csv | cut -d ',' -f 1,2 >> filtered_by_same_value_collision.csv

echo "tx_a,tx_b" > filtered_by_indirect_dependencies_recursive.csv
grep -E 'indirect_dependencies_recursive' mine/tod_candidates_evaluation.csv | cut -d ',' -f 1,2 >> filtered_by_indirect_dependencies_recursive.csv

echo "tx_a,tx_b" > filtered_by_indirect_dependencies_quick.csv
grep -E 'indirect_dependencies_quick' mine/tod_candidates_evaluation.csv | cut -d ',' -f 1,2 >> filtered_by_indirect_dependencies_quick.csv

echo "tx_a,tx_b" > has_indirect_dependencies.csv
grep -E '(0x[a-f0-9]+,0x[a-f0-9]+),True' mine-indirect-dependencies/tod_check_indirect_dependencies.csv | cut -d ',' -f 1,2 >> has_indirect_dependencies.csv

python3 ../../../scripts/compare_tods.py ../rq1-3_search.csv has_indirect_dependencies.csv filtered_by_same_value_collision.csv filtered_by_indirect_dependencies_quick.csv > comparison_indirect_dependencies.csv