# Results from the T-RACE paper

README is WIP...


## Commands used for the experiments

Main evaluation:

`t_race run --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999`

Evaluation mining:

`t_race mine --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999 --quick-stats --evaluate-candidates-csv rq1-3_search.csv`

`t_race mine --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999 --quick-stats --evaluate-candidates-csv rq1-3_search.csv --extract-indirect-dependencies`
`t_race check --check-indirect-dependencies --tod-candidates tod_candidates_evaluation.csv`

`t_race mine --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999 --quick-stats --evaluate-candidates-csv rq1-3_search.csv --extract-limit-representatives`

Evaluation check:

`t_race check --check-props-for-all --tod-candidates-csv rq1-3_search.csv`



`grep '"approximately TOD": true' out/tod_check_details.jsonl | sed -r 's/^[^0]+(0x[0-9a-f]+)[^0]+(0x[0-9a-f]+).*$/\1,\2/' > approximately_tod.csv`