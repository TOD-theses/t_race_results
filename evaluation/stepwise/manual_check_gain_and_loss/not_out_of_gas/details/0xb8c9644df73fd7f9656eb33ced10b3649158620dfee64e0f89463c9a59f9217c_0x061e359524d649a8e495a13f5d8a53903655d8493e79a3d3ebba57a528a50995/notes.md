# TOD attack analysis

Transactions:
- T_A: [0xb8c9644df73fd7f9656eb33ced10b3649158620dfee64e0f89463c9a59f9217c](https://etherscan.io/tx/0xb8c9644df73fd7f9656eb33ced10b3649158620dfee64e0f89463c9a59f9217c)
- T_B: [0x061e359524d649a8e495a13f5d8a53903655d8493e79a3d3ebba57a528a50995](https://etherscan.io/tx/0x061e359524d649a8e495a13f5d8a53903655d8493e79a3d3ebba57a528a50995)

## Ground truth

### Attacker
Asset changes for: [0x1ae71Aa9DcDEe0eEf5Da60586D9501D9b54B4Ee0](https://etherscan.io/address/0x1ae71Aa9DcDEe0eEf5Da60586D9501D9b54B4Ee0)
- ERC20_TOKEN (+0x5162) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


### Victim
Asset changes for: [0xDB208b323A9f0F26E29FEDd9D1DA3A4Cff902D6E](https://etherscan.io/address/0xDB208b323A9f0F26E29FEDd9D1DA3A4Cff902D6E)
- ERC20_TOKEN (-0xa4590e) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


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

