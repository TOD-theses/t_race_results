# TOD attack analysis

Transactions:
- T_A: [0x9266d411b9a5c641672d23e6daeeddb889927a616d5c217afd8504fdcf73426f](https://etherscan.io/tx/0x9266d411b9a5c641672d23e6daeeddb889927a616d5c217afd8504fdcf73426f)
- T_B: [0x42cb6a4d4ec2a9e73dbaa03c478c556145152b3df21f91554b8db956aef623a5](https://etherscan.io/tx/0x42cb6a4d4ec2a9e73dbaa03c478c556145152b3df21f91554b8db956aef623a5)

## Ground truth

### Attacker
Asset changes for: [0x491336a7d4E49996f5F4C07D51dfC4eB501a541E](https://etherscan.io/address/0x491336a7d4E49996f5F4C07D51dfC4eB501a541E)
- ERC20_TOKEN (+0x2765) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


### Victim
Asset changes for: [0x472e24363D99964c001f43Dc31e98B782c3CEA98](https://etherscan.io/address/0x472e24363D99964c001f43Dc31e98B782c3CEA98)
- ERC20_TOKEN (-0x5dce6271dcf9a74b) https://etherscan.io/token/0x7866E48C74CbFB8183cd1a929cd9b95a7a5CB4F4


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

