# TOD attack analysis

Transactions:
- T_A: [0xf418139f1cf3be22d40b6508de36bde2d61b5aa7a8bc0636230fc56943897081](https://etherscan.io/tx/0xf418139f1cf3be22d40b6508de36bde2d61b5aa7a8bc0636230fc56943897081)
- T_B: [0xa56c9258f032396fbe1f36c044feeebd4d5ab2d943d160c81700087191ca5abe](https://etherscan.io/tx/0xa56c9258f032396fbe1f36c044feeebd4d5ab2d943d160c81700087191ca5abe)

## Ground truth

### Attacker
Asset changes for: [0xc1f7d778dC3EF09FEad1ebf809C0C25718dBC0Ef](https://etherscan.io/address/0xc1f7d778dC3EF09FEad1ebf809C0C25718dBC0Ef)
- ERC20_TOKEN (+0x767c) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


### Victim
Asset changes for: [0x12EC184d251C43bEC97EF9edA506CB02587D9992](https://etherscan.io/address/0x12EC184d251C43bEC97EF9edA506CB02587D9992)
- ERC20_TOKEN (-0x258097) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: False
- attacker_bot_gain: False
- attacker_bot_loss: False
- victim_gain: True
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

