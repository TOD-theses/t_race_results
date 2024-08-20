# TOD attack analysis

Transactions:
- T_A: [0xba5bf69ce151310936d427d3359c43a6910c2381d5a2c8cf33a807e478c50cc4](https://etherscan.io/tx/0xba5bf69ce151310936d427d3359c43a6910c2381d5a2c8cf33a807e478c50cc4)
- T_B: [0x6d9cfdca4c232ca706455c44ac40d05723a2e00b0213c7dadf8df43154ac7f7d](https://etherscan.io/tx/0x6d9cfdca4c232ca706455c44ac40d05723a2e00b0213c7dadf8df43154ac7f7d)

## Ground truth

### Attacker
Asset changes for: [0xA9CE7b858B81Efc914c881E648f3AEa3F3980B12](https://etherscan.io/address/0xA9CE7b858B81Efc914c881E648f3AEa3F3980B12)
- ERC20_TOKEN (+0x9a8) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


### Victim
Asset changes for: [0xF0EAf0C77c1362aD4dE668755be5559EB47cFB9f](https://etherscan.io/address/0xF0EAf0C77c1362aD4dE668755be5559EB47cFB9f)
- ERC20_TOKEN (-0xe1e8bc2696fdaaff5) https://etherscan.io/token/0x4bD70556ae3F8a6eC6C4080A0C327B24325438f3


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

