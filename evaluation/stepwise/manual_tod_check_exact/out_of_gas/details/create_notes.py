
import os
from pathlib import Path


def create_notes(tx_a: str, tx_b: str):
    return f"""# Out of gas analysis

Transactions:
- T_A: [{tx_a}](https://etherscan.io/tx/{tx_a})
- T_B: [{tx_b}](https://etherscan.io/tx/{tx_b})

## Reverted according to our traces?



## Reverted according to Etherscan?

"""

def main():
    for entry in os.listdir():
        if not os.path.isfile(entry):
            tx_a, tx_b = entry.split('_')
            print(tx_a, tx_b)
            notes = create_notes(tx_a, tx_b)
            with open(Path(entry) / 'notes.md', 'w') as notes_file:
                notes_file.write(notes)

if __name__ == '__main__':
    main()
