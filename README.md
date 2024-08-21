# Results from the T-RACE paper

## Samples

The results for the TOD candidate mining and the TOD detection experiments are in the [sample](./sample/) folder.

Relevant files are:
- mining_stats.json: contains information on how many candidates were filtered by each filter
- tod_candidates.csv: a CSV of the remaining TOD candidates
- check_comparison.csv: a CSV containing the comparison between approximation and exact TOD

These were run with an older version of t_race, thus the output format is slightly different than for the rest of the dataset, however similar results can be obtained with these commands:

- `t_race mine --blocks 19830547-19830646 --window-size 25`
- `t_race mine --blocks 19830547-19830646 --window-size 25 --duplicates-limit 10`
- `t_race check` (requires `tod_candidates.csv` to exist, the details contain the results for the approximation)

Run `t_race stats` to create the graphics based on the results.

## Evaluation

The [evaluation](./evaluation/) folder contains the results of the evaluation runs and notes for the manual evaluation.

Relevant files/folders:
- rq1-3_search.csv/jsonl: the ground truth formatted as CSV/JSONL

For manual evaluations we use following folders:
- details/{tx_a}_{tx_b}/notes.md: for manual evaluations, this contains the notes of analyzing an attack
- details/{tx_a}_{tx_b}/traces.tar.gz: compressed traces of the normal and reverse scenarios


### Overall

This folder contains the results and evaluations for running all three components together.

Commands:
- `t_race run --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999`

Relevant files/folders:
- [eval](evaluation/overall/eval): output from running t_race, containing details of each TOD candidate check and attack analysis in the "_details.jsonl" files
- [comparison.csv](evaluation/overall/comparison.csv): CVS describing which TOD candidates are part of which step

#### Manual analysis of attacks not in ground truth

Relevant files/folders:
- [attacks_low_block_dist.csv](evaluation/overall/manual_attacks_not_in_ground_truth/attacks_low_block_dist.csv): attacks our tool found within the same block window size as the ground truth

#### Manual analysis of ERC-20 multiple withdrawal attacks

Relevant files/folders:
- [erc20_multiple_withdrawals.csv](evaluation/overall/manual_erc20_multiple_withdrawal/erc20_multiple_withdrawals.csv): transaction pairs fulfilling the definition

#### Manual analysis of Securify properties

Relevant files/folders:
- attacks.csv: found transaction pairs fulfilling the properties
- sample.csv: a sample of 20 from the attacks

### Stepwise

This folder contains the results from evaluation the individual components.

The `create_*` scripts are used to merge several results from the tool and create `comparison_*.csv` files out of them. The `count_*` scripts to give basic statistics about them.

#### Mining

Commands:
- `t_race mine --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999 --quick-stats --evaluate-candidates-csv rq1-3_search.csv`
- `t_race mine --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999 --quick-stats --evaluate-candidates-csv rq1-3_search.csv --extract-indirect-dependencies`
- `t_race check --check-indirect-dependencies --tod-candidates tod_candidates_evaluation.csv`
- `t_race mine --window-size 25 --duplicates-limit 10 --blocks 11299000-11299999 --quick-stats --evaluate-candidates-csv rq1-3_search.csv --extract-limit-representatives`

Relevant files/folders:
- [mine/tod_candidates_evaluation.csv](evaluation/stepwise/mine/tod_candidates_evaluation.csv): describes which attacks from the ground truth have been filtered by which filter
- [mine-indirect-dependencies/tod_candidates_evaluation.csv](evaluation/stepwise/mine-indirect-dependencies/tod_candidates_evaluation.csv): contains the potential indirect dependency paths
- [mine-indirect-dependencies/tod_check_indirect_dependencies.csv](evaluation/stepwise/mine-indirect-dependencies/tod_check_indirect_dependencies.csv): contains attacks where we found an indirect dependency according to our TOD check (and the intermediary transactions as a witness)
- [mine-duplicate-limit/tod_candidates_evaluation.csv](evaluation/stepwise/mine-duplicate-limit/tod_candidates_evaluation.csv): contains attacks that were filtered by duplicate limits and maps them to transactions that cover their collisions

#### TOD detection and attack analysis

Commands:
- `t_race check --check-props-for-all --tod-candidates-csv rq1-3_search.csv`

Relevant files/folders:
- [check](evaluation/stepwise/check): the results of running t_race, containing an overview and details of the TOD detection and TOD attack analysis for each attack

##### Manual evaluation of TOD detection

Relevant files/folders:
- [missed_exact.csv](evaluation/stepwise/manual_tod_check_exact/missed_exact.csv): contains all attacks that our method does not report as TOD
- [out_of_gas/missed.csv](evaluation/stepwise/manual_tod_check_exact/out_of_gas/missed.csv): contains all attacks labelled "out of gas" that we analyzed without errors as not TOD
- [not_out_of_gas/missed.csv](evaluation/stepwise/manual_tod_check_exact/not_out_of_gas/missed.csv): contains all attacks not labelled "out of gas" that we analyzed without errors and marked as not TOD

##### Manual evaluation of attacker gain and victim loss

Relevant files/folders:
- [missed.csv](evaluation/stepwise/manual_check_gain_and_loss/missed.csv): contains all attacks we did not mark as an attack
- [not_out_of_gas/missed.csv](evaluation/stepwise/manual_check_gain_and_loss/not_out_of_gas/missed.csv): contains all attacks where our analysis ran without errors and which are not labelled "out of gas"
