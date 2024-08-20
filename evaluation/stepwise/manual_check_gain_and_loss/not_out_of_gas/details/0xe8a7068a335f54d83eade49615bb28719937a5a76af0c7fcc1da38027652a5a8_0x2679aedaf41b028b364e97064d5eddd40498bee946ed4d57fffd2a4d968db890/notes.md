# TOD attack analysis

Transactions:
- T_A: [0xe8a7068a335f54d83eade49615bb28719937a5a76af0c7fcc1da38027652a5a8](https://etherscan.io/tx/0xe8a7068a335f54d83eade49615bb28719937a5a76af0c7fcc1da38027652a5a8)
- T_B: [0x2679aedaf41b028b364e97064d5eddd40498bee946ed4d57fffd2a4d968db890](https://etherscan.io/tx/0x2679aedaf41b028b364e97064d5eddd40498bee946ed4d57fffd2a4d968db890)

## Ground truth

### Attacker
Asset changes for: [0x7e9997a38A439b2be7ed9c9C4628391d3e055D48](https://etherscan.io/address/0x7e9997a38A439b2be7ed9c9C4628391d3e055D48)
- ERC20_TOKEN (+0x7f4601) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


### Victim
Asset changes for: [0x33eEc719Cc0849775d55A7eB453b6EF9cbA1d518](https://etherscan.io/address/0x33eEc719Cc0849775d55A7eB453b6EF9cbA1d518)
- ERC20_TOKEN (-0x2a) https://etherscan.io/token/0x7e9997a38A439b2be7ed9c9C4628391d3e055D48


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: True
- attacker_bot_gain: False
- attacker_bot_loss: True
- victim_gain: False
- victim_loss: False

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

