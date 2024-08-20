# TOD attack analysis

Transactions:
- T_A: [0xf1ebc786191fb51dfd91db3fce0fe9d96a72c6128b1d066b68d6144d39e71cae](https://etherscan.io/tx/0xf1ebc786191fb51dfd91db3fce0fe9d96a72c6128b1d066b68d6144d39e71cae)
- T_B: [0xe58749f73251e201854a7daeb4212bd542f58bf09ce95d70829fb7ade67dce80](https://etherscan.io/tx/0xe58749f73251e201854a7daeb4212bd542f58bf09ce95d70829fb7ade67dce80)

## Ground truth

### Attacker
Asset changes for: [0x0000000000007F150Bd6f54c40A34d7C3d5e9f56](https://etherscan.io/address/0x0000000000007F150Bd6f54c40A34d7C3d5e9f56)
- ETHER (+0x32a43e7e0d8f70)
- ERC20_TOKEN (+0x18097aaeb8) https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F
- ERC20_TOKEN (+0x17194089) https://etherscan.io/token/0xA8e7AD77C60eE6f30BaC54E2E7c0617Bd7B5A03E


### Victim
Asset changes for: [0x134C6b07C5f1B9131aABAF1FAe3618a42eCc3D31](https://etherscan.io/address/0x134C6b07C5f1B9131aABAF1FAe3618a42eCc3D31)
- ETHER (-0x26689f9fe23c8f)


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: False
- attacker_eoa_loss: False
- attacker_bot_gain: False
- attacker_bot_loss: False
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

