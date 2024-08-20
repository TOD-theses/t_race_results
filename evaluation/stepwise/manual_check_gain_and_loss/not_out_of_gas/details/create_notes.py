
from collections import defaultdict
from dataclasses import dataclass
import json
import os
from pathlib import Path

@dataclass
class Attack:
    attacker_asset_changes: dict[tuple[str, str, str | None], int]
    victim_asset_changes: dict[tuple[str, str, str | None], int]

def stringify_asset_changes(asset_changes: dict[tuple[str, str, str | None], int]) -> str:
    changes_by_address: dict[str, list[tuple[str, str | None, int]]] = defaultdict(list)
    for (type, address, token_contract), amount in asset_changes.items():
        changes_by_address[address].append((type, token_contract, amount))

    s = ""
    for address, changes in changes_by_address.items():
        s += f"Asset changes for: [{address}](https://etherscan.io/address/{address})\n"
        for type, token_contract, amount in changes:
            s += f"- {type} ({'+' if amount > 0 else ''}{hex(amount)})"
            if token_contract:
                s += f" https://etherscan.io/token/{token_contract}"
            s += "\n"

    return s


def load_attacks(path: Path) -> dict[tuple[str, str], Attack]:
    attacks = {}
    with open(path) as f:
        for line in f:
            attack = json.loads(line)
            attacks[(attack['tx_a'], attack['tx_b'])] = Attack(
                attacker_asset_changes=get_asset_changes(attack['attackerProfits']['attack'], attack['attackerProfits']['attackFree']),
                victim_asset_changes=get_asset_changes(attack['victimProfits']['attack'], attack['victimProfits']['attackFree']),
            )

    return attacks

def load_properties(path: Path) -> dict[tuple[str, str], dict]:
    properties = {}
    with open(path) as f:
        for line in f:
            details = json.loads(line)['details']
            properties[(details['tx_a'], details['tx_b'])] = details['gain_and_loss']['properties']

    return properties

def get_asset_changes(attack: dict, attack_free: dict) -> dict[tuple[str, str, str | None], int]:
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

def create_notes(tx_a: str, tx_b: str, attack: Attack, properties: dict):
    return f"""# TOD attack analysis

Transactions:
- T_A: [{tx_a}](https://etherscan.io/tx/{tx_a})
- T_B: [{tx_b}](https://etherscan.io/tx/{tx_b})

## Ground truth

### Attacker
{stringify_asset_changes(attack.attacker_asset_changes)}

### Victim
{stringify_asset_changes(attack.victim_asset_changes)}

## Tool properties output

{chr(10).join([f'- {key}: {val}' for key, val in properties.items()])}

## Manually parsed logs

Containing attacker:

| Normal T_A | Reverse T_A | Is gain? |
|------------|-------------|----------|
|            |             |          |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|
|            |             |          |

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|
|            |             |          |

| Normal T_B | Reverse T_B | Is loss? |
|------------|-------------|----------|
|            |             |          |



## Reverted call contexts?



## Normal scenario logs match Etherscan logs?



## Other notes

"""

def main():
    attacks = load_attacks(Path('../sample_ground_truth.jsonl'))
    properties = load_properties(Path('../sample_tod_properties_details.jsonl'))

    for entry in os.listdir():
        if not os.path.isfile(entry):
            tx_a, tx_b = entry.split('_')
            attack = attacks[(tx_a, tx_b)]
            props = properties[(tx_a, tx_b)]
            print(tx_a, tx_b)
            notes = create_notes(tx_a, tx_b, attack, props)
            with open(Path(entry) / 'notes.md', 'w') as notes_file:
                notes_file.write(notes)

if __name__ == '__main__':
    main()
