from collections import defaultdict
import json
from pathlib import Path
from typing import Counter, Iterable

def analyze(attacks: Iterable[dict]):
    types = Counter()

    for attack in attacks:
        attacker_changes = get_asset_changes(attack['attackerProfits']['attack'], attack['attackerProfits']['attackFree'])
        victim_changes = get_asset_changes(attack['victimProfits']['attack'], attack['victimProfits']['attackFree'])

        types_in_attack = set()

        for type, address, token_contract in attacker_changes:
            types_in_attack.add(type)
        for type, address, token_contract in victim_changes:
            types_in_attack.add(type)

        types.update([tuple(sorted(types_in_attack))])
    
    print(types)


def get_asset_changes(attack: dict, attack_free: dict):
    # maps (asset type, address, token_contract) to the amount of assets gained/lost
    asset_changes: dict[tuple[str, str, str | None], int] = defaultdict(int)
    
    for change in attack:
        type = change['type']
        account = change['account']
        amount = int(change['amount'])
        contract = change.get('contract')

        asset_changes[(type, account, contract)] += amount

    for change in attack_free:
        type = change['type']
        account = change['account']
        amount = int(change['amount'])
        contract = change.get('contract')

        asset_changes[(type, account, contract)] -= amount

    return {key: amount for key, amount in asset_changes.items() if amount != 0}

def load_jsonl(path: Path) -> Iterable[dict]:
    with open(path) as f:
        for line in f:
            yield json.loads(line)

def main():
    analyze(load_jsonl(Path('ground_truth.jsonl')))

if __name__ == '__main__':
    main()