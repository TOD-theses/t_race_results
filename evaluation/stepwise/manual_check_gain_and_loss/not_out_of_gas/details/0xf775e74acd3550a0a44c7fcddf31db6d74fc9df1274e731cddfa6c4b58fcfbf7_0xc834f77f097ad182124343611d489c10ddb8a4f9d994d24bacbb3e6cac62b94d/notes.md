# TOD attack analysis

Transactions:
- T_A: [0xf775e74acd3550a0a44c7fcddf31db6d74fc9df1274e731cddfa6c4b58fcfbf7](https://etherscan.io/tx/0xf775e74acd3550a0a44c7fcddf31db6d74fc9df1274e731cddfa6c4b58fcfbf7)
- T_B: [0xc834f77f097ad182124343611d489c10ddb8a4f9d994d24bacbb3e6cac62b94d](https://etherscan.io/tx/0xc834f77f097ad182124343611d489c10ddb8a4f9d994d24bacbb3e6cac62b94d)

## Ground truth

### Attacker
Asset changes for: [0x106f6651Eb3Dbf96952524d6176618aB9D8DD27C](https://etherscan.io/address/0x106f6651Eb3Dbf96952524d6176618aB9D8DD27C)
- ETHER (+0x4cb465a35ff)


### Victim
Asset changes for: [0x4FF92DD0C8EA4D51cf46aE38a8d79Cb66F7618FA](https://etherscan.io/address/0x4FF92DD0C8EA4D51cf46aE38a8d79Cb66F7618FA)
- ERC20_TOKEN (-0x2e246cf95132827a) https://etherscan.io/token/0x1E15abF152067e9Fe4A48bbf094A71f5bB16325D


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: False
- attacker_bot_gain: True
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

