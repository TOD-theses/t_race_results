from collections import Counter
import csv
from pathlib import Path


def count(path: Path, candidates: set[tuple[str, str]]):
    counter_covered = 0
    counter_covered_single = 0
    counter_single_representatives = Counter()
    counter_total = 0

    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (row['tx_a'], row['tx_b']) not in candidates:
                continue
            counter_total += 1
            if row['covered'] == 'True':
                counter_covered += 1
                representatives = row['representatives'].split('|')
                if len(representatives) == 1:
                    counter_covered_single += 1
                    counter_single_representatives.update(representatives)
    
    print('Total', counter_total)
    print('Covered', counter_covered)
    print('Covered single', counter_covered_single)
    n = 3
    common_representatives = counter_single_representatives.most_common(n)
    print(f'{n} most common representatives for single coverage:')
    print(*common_representatives, sep='\n')
    print(f'Together they represent: {sum(n for _, n in common_representatives)}')

def get_candidates_removed_by_limit(path: Path) -> set[tuple[str, str]]:
    candidates = set()
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'limited' in row['filtered_by']:
                candidates.add((row['tx_a'], row['tx_b']))
    
    return candidates


def main():
    filtered_candidates = get_candidates_removed_by_limit(Path('mine') / 'tod_candidates_evaluation.csv')
    count(Path('mine-duplicate-limit') / 'tod_candidates_evaluation.csv', filtered_candidates)

if __name__ == '__main__':
    main()