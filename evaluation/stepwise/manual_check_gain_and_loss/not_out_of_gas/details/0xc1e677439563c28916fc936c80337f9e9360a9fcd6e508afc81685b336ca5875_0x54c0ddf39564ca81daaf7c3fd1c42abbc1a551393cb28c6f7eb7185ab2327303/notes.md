# TOD attack analysis

Transactions:
- T_A: [0xc1e677439563c28916fc936c80337f9e9360a9fcd6e508afc81685b336ca5875](https://etherscan.io/tx/0xc1e677439563c28916fc936c80337f9e9360a9fcd6e508afc81685b336ca5875)
- T_B: [0x54c0ddf39564ca81daaf7c3fd1c42abbc1a551393cb28c6f7eb7185ab2327303](https://etherscan.io/tx/0x54c0ddf39564ca81daaf7c3fd1c42abbc1a551393cb28c6f7eb7185ab2327303)

## Ground truth

### Attacker
Asset changes for: [0x0000000000007F150Bd6f54c40A34d7C3d5e9f56](https://etherscan.io/address/0x0000000000007F150Bd6f54c40A34d7C3d5e9f56)
- ETHER (+0x2b9b399d19e591)
- ERC20_TOKEN (+0xb932448004f) https://etherscan.io/token/0x7866E48C74CbFB8183cd1a929cd9b95a7a5CB4F4


### Victim
Asset changes for: [0x1c58DEEf8c532304F1d90a1c03d73734aF55F2BA](https://etherscan.io/address/0x1c58DEEf8c532304F1d90a1c03d73734aF55F2BA)
- ERC20_TOKEN (-0x3c8cd3617f43467c) https://etherscan.io/token/0x7866E48C74CbFB8183cd1a929cd9b95a7a5CB4F4


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: False
- attacker_eoa_loss: False
- attacker_bot_gain: True
- attacker_bot_loss: True
- victim_gain: False
- victim_loss: True

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

