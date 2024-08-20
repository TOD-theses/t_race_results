# TOD attack analysis

Transactions:
- T_A: [0xc1fa212aaaa26adf4df28b20f65ee598161a7b7404764250b698b8304543ad9b](https://etherscan.io/tx/0xc1fa212aaaa26adf4df28b20f65ee598161a7b7404764250b698b8304543ad9b)
- T_B: [0x997884afe752dcfaf293d05b925b466d9e7420cc5ad2e38a80a57765caceee10](https://etherscan.io/tx/0x997884afe752dcfaf293d05b925b466d9e7420cc5ad2e38a80a57765caceee10)

## Ground truth

### Attacker
Asset changes for: [0x37Bf78fA8853CEE7df39280e70e38f3e163E44c4](https://etherscan.io/address/0x37Bf78fA8853CEE7df39280e70e38f3e163E44c4)
- ERC20_TOKEN (+0x2d82d) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


### Victim
Asset changes for: [0x9009ebB15B2865E90200e84bbebd8C8e01364fC5](https://etherscan.io/address/0x9009ebB15B2865E90200e84bbebd8C8e01364fC5)
- ERC20_TOKEN (-0x3dde65ef869a68c) https://etherscan.io/token/0x28cb7e841ee97947a86B06fA4090C8451f64c0be


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

