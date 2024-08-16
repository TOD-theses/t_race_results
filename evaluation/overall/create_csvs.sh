set -e

cut eval/tod_candidates.csv -d ',' -f 1,2 > tod_candidate.csv
echo "tx_a,tx_b" > tod_overall.csv
grep -E '(0x[a-f0-9]+,0x[a-f0-9]+),TOD' eval/tod_check.csv | cut -d ',' -f 1,2 >> tod_overall.csv
echo "tx_a,tx_b" > property_gain_and_loss.csv
grep -E '(0x[a-f0-9]+,0x[a-f0-9]+),True' eval/tod_properties.csv | cut -d ',' -f 1,2 >> property_gain_and_loss.csv

compare_tods.py ../rq1-3_search.csv tod_candidate.csv tod_overall.csv property_gain_and_loss.csv > comparison.csv


echo "tx_a,tx_b" > erc20_multiple_withdrawals.csv
grep -E '(\w+,){7}True' eval/tod_properties.csv >> erc20_multiple_withdrawals.csv
