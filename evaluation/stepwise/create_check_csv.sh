set -e

echo "tx_a,tx_b" > tod_overall.csv
grep -E '(0x[a-f0-9]+,0x[a-f0-9]+),TOD' check/tod_check.csv | cut -d ',' -f 1,2 >> tod_overall.csv

echo "tx_a,tx_b" > tod_approximation.csv
grep '"approximately TOD": true' check/tod_check_details.jsonl | sed -r 's/^[^0]+(0x[0-9a-f]+)[^0]+(0x[0-9a-f]+).*$/\1,\2/' >> tod_approximation.csv

echo "tx_a,tx_b" > property_gain_and_loss.csv
grep -E '(0x[a-f0-9]+,0x[a-f0-9]+),True' check/tod_properties.csv | cut -d ',' -f 1,2 >> property_gain_and_loss.csv

python3 compare_tods.py ../rq1-3_search.csv tod_overall.csv tod_approximation.csv property_gain_and_loss.csv > comparison_check.csv