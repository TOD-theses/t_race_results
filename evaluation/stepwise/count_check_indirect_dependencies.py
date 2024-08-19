from collections import defaultdict
import csv
from pathlib import Path
from typing import Literal

CHECK_RESULT = Literal['TOD'] | Literal['not TOD'] | Literal['error'] | Literal['replay diverged']


def load_dependencies(path: Path):
    dependencies: dict[tuple[str, str], list[str]] = defaultdict(list)

    with open(path, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            dependencies[(row['tx_a'], row['tx_b'])].append(row['path'].split('|')[1])

    return dependencies

def load_check_results(path: Path):
    results: dict[tuple[str, str], CHECK_RESULT] = {}

    with open(path, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            results[(row['tx_a'], row['tx_b'])] = row['result'] # type: ignore

    return results

def merge_dependencies_with_results(dependencies: dict[tuple[str, str], list[str]], results: dict[tuple[str, str], CHECK_RESULT]):
    deps_with_results: dict[tuple[str, str], list[tuple[CHECK_RESULT, CHECK_RESULT]]] = defaultdict(list)
    for candidate in dependencies:
        tx_a, tx_b = candidate

        for tx_x in dependencies[candidate]:
            result_a = results[(tx_a, tx_x)]
            result_b = results[(tx_x, tx_b)]
            deps_with_results[candidate].append((result_a, result_b))

    return deps_with_results

def main():
    dependencies = load_dependencies(Path('mine-indirect-dependencies') / 'tod_candidates_evaluation.csv')
    results = load_check_results(Path('mine-indirect-dependencies') / 'tod_check.csv')

    merged = merge_dependencies_with_results(dependencies, results)

    counts = {
        'total': 0,
        'positive': 0,
        'failed': 0,
        'negative': 0,
    }

    for candidate, results in merged.items():
        counts['total'] += 1
        if any(a == 'TOD' and b == 'TOD' for a, b in results):
            counts['positive'] += 1
        elif any(a not in ['TOD', 'not TOD'] or b not in ['TOD', 'not TOD'] for a, b in results):
            counts['failed'] += 1
        else:
            assert any(a == 'not TOD' or b == 'not TOD' for a, b in results), f'Unexpected results: {candidate} - {results}'
            counts['negative'] += 1

    print(counts)

if __name__ == '__main__':
    main()