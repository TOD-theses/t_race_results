# TOD checker output

Transactions:
- T_A: [0xb8c720a10d03fe299626a5e514ab1f4d0d1d8d44493b161f972c03a63df23462](https://etherscan.io/tx/0xb8c720a10d03fe299626a5e514ab1f4d0d1d8d44493b161f972c03a63df23462)
- T_B: [0x2c6f4af735d0490284f11dbd3192df4d9ecc0d42898ec826cd8be8d4982fa1a3](https://etherscan.io/tx/0x2c6f4af735d0490284f11dbd3192df4d9ecc0d42898ec826cd8be8d4982fa1a3)


Attacker: [0xf8fff4959b9cdeaeb0ff03199d7e51cb438e92c6](https://etherscan.io/address/0xf8fff4959b9cdeaeb0ff03199d7e51cb438e92c6)
Victim: [0x50c57f86b1e0f766e458838a2e13eb75e91d7692](https://etherscan.io/address/0x50c57f86b1e0f766e458838a2e13eb75e91d769)

Attacker gain tokens:
- ERC-20 [cETH](https://etherscan.io/token/0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5)

Victim loss tokens:
- ERC-20 [COMP](https://etherscan.io/token/0xc00e94cb662c3520282e6f5717214004a7f26888)

# Manually parsed logs

Containing attacker:

| Normal T_A                                 | Reverse T_A | Is gain? |
|--------------------------------------------|-------------|----------|
| Transfer(0x4dd..., 0xf8f..., 0x3a1f7efc9c) | <reverted>  | Yes      |

| Normal T_B                                 | Reverse T_B | Is gain?  |
|--------------------------------------------|-------------|-----------|

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                       | Reverse T_B                                      | Is loss?  |
|--------------------------------------------------|--------------------------------------------------|-----------|
| Transfer(0x3d9..., 0x50c..., 0x7fce9d733515ee0)  | Transfer(0x3d9..., 0x50c..., 0x7fce9d782cac6f0)  | Yes       |
| Transfer(0x3d9..., 0x50c..., 0x2af81a35cd1732f9) | Transfer(0x3d9..., 0x50c..., 0x2af81a35cd1732f9) | identical |
| Transfer(0x962..., 0x50c..., 0x0)                | Transfer(0x962..., 0x50c..., 0x0)                | identical |


# Reverted call contexts?

T_A reverse

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

If we considered transaction value, then we would have attacker loss because of the transaction revert.