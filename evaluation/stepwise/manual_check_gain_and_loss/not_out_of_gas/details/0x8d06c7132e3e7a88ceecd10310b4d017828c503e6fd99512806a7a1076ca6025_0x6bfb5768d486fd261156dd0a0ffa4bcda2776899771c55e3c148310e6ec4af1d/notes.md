# TOD attack analysis

Transactions:
- T_A: [0x8d06c7132e3e7a88ceecd10310b4d017828c503e6fd99512806a7a1076ca6025](https://etherscan.io/tx/0x8d06c7132e3e7a88ceecd10310b4d017828c503e6fd99512806a7a1076ca6025)
- T_B: [0x6bfb5768d486fd261156dd0a0ffa4bcda2776899771c55e3c148310e6ec4af1d](https://etherscan.io/tx/0x6bfb5768d486fd261156dd0a0ffa4bcda2776899771c55e3c148310e6ec4af1d)

## Ground truth

### Attacker
Asset changes for: [0x14D0480FbE1E40F96702C36D6B0c9b98eB5b27f0](https://etherscan.io/address/0x14D0480FbE1E40F96702C36D6B0c9b98eB5b27f0)
- ETHER (+0x1eb4113bf7c)


### Victim
Asset changes for: [0x11fFF88d6d1eea7742566a32BE02173AEb71a814](https://etherscan.io/address/0x11fFF88d6d1eea7742566a32BE02173AEb71a814)
- ERC20_TOKEN (-0x150f89d27ac54cfa) https://etherscan.io/token/0x5b3F693EfD5710106eb2Eac839368364aCB5a70f


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: False
- attacker_bot_gain: True
- attacker_bot_loss: False
- victim_gain: True
- victim_loss: False

## Manually parsed logs

Containing attacker (not investigated)

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                          | Reverse T_B                                           | Is loss?  |
|-----------------------------------------------------|-------------------------------------------------------|-----------|
| Transfer@dac(0x11f..., 0xd4a..., 0x77359400)        | Transfer@dac(0x11f..., 0xd4a..., 0x77359400)          | identical |
| Transfer@5b3(0xe43..., 0x11f..., 6494cdee1362b67f2) | Transfer@5b3(0xe43..., 0x11f..., 0x648e570316028598a) | No        |



## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Yes

# First divergence

## T_B

SLOAD diverges at slot 0x8 (address 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, pc 3475):
- Normal: 5fb8a90b00000000000000005a0016c989c4000000002962f63496820f6c824a
- Reverse: 5fb8a8dd00000000000000005a030fa7fd69000000002961974d763c394aaba6

This is written by T_A, therefore we overwrite it. However, the value written by T_A does not match the normal scenario value, hence an intermediary transaction also has written to this storage slot.

## Other notes

Victim gain, not loss according to our traces.