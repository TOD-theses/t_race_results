# TOD attack analysis

Transactions:
- T_A: [0xbbfd02304714a7fa65be1a42f6fecb1873722a6b9497a25a0a1e36733f66cb39](https://etherscan.io/tx/0xbbfd02304714a7fa65be1a42f6fecb1873722a6b9497a25a0a1e36733f66cb39)
- T_B: [0xf87214bbc40772d9fe64e2488c2c72d67574c9592f1330c7236547e14f162ad8](https://etherscan.io/tx/0xf87214bbc40772d9fe64e2488c2c72d67574c9592f1330c7236547e14f162ad8)

## Ground truth

### Attacker
Asset changes for: [0x0000000000007F150Bd6f54c40A34d7C3d5e9f56](https://etherscan.io/address/0x0000000000007F150Bd6f54c40A34d7C3d5e9f56)
- ETHER (+0x1ffa053b5ddaf9)
- ERC20_TOKEN (+0x2e) https://etherscan.io/token/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48


### Victim
Asset changes for: [0x128572c25F55a04578161605b714B2cBBdf1273F](https://etherscan.io/address/0x128572c25F55a04578161605b714B2cBBdf1273F)
- ERC20_TOKEN (-0x3cf63ceb6) https://etherscan.io/token/0x5Dc02Ea99285E17656b8350722694c35154DB1E8


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

