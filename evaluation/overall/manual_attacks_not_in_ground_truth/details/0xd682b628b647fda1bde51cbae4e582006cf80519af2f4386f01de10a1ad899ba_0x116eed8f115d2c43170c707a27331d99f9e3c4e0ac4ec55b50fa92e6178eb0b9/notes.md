# TOD checker output

Transactions:
- T_A: [0xd682b628b647fda1bde51cbae4e582006cf80519af2f4386f01de10a1ad899ba](https://etherscan.io/tx/0xd682b628b647fda1bde51cbae4e582006cf80519af2f4386f01de10a1ad899ba)
- T_B: [0x116eed8f115d2c43170c707a27331d99f9e3c4e0ac4ec55b50fa92e6178eb0b9](https://etherscan.io/tx/0x116eed8f115d2c43170c707a27331d99f9e3c4e0ac4ec55b50fa92e6178eb0b9)


Attacker: [0xdf7ebadb3ec9bb63e9639600ce9783ebd2fa193c](https://etherscan.io/address/0xdf7ebadb3ec9bb63e9639600ce9783ebd2fa193c)
Victim: [0xef80d1b797ab9faf01daa46341d99effde776e24](https://etherscan.io/address/0xef80d1b797ab9faf01daa46341d99effde776e24)

Attacker gain tokens:
- ERC-20 [CP3R](https://etherscan.io/token/0x7ef1081ecc8b5b5b130656a41d4ce4f89dbbcc8c)

Victim loss tokens:
- ERC-20 [CP3R](https://etherscan.io/token/0x7ef1081ecc8b5b5b130656a41d4ce4f89dbbcc8c)

# Manually parsed logs

Containing attacker:

| Normal T_A                                               | Reverse T_A | Is gain? |
|----------------------------------------------------------|-------------|----------|
| Transfer@7ef...(0x3ea..., 0xdf7..., 0x4a620dfa4088be000) | <reverted>  | Yes      |
| Transfer@df7...(0x0..., 0xdf7..., 0x4a620dfa4088be000)   | <reverted>  |          |
| Transfer@df7...(0xdf7..., 0xa29..., 0x4a620dfa4088be000) | <reverted>  |          |

| Normal T_B                                               | Reverse T_B                                              | Is gain?  |
|----------------------------------------------------------|----------------------------------------------------------|-----------|
| Transfer@7ef...(0xdf7..., 0xef8..., 0x18493fba64ef00000) | Transfer@7ef...(0xdf7..., 0xef8..., 0x18493fba64ef00000) | identical |

Overall:
- attacker gains 0x4a620dfa4088be000 = 85757790000000000000 CP3R

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                               | Reverse T_B                                              | Is loss?  |
|----------------------------------------------------------|----------------------------------------------------------|-----------|
| Transfer@df7...(0xa29..., 0xef8..., 0x18493fba64ef00000) | Transfer@df7...(0xa29..., 0xef8..., 0x18493fba64ef00000) | identical |
| Transfer@7ef...(0xa29..., 0xef8..., 0x4ef2d495915fd10)   | Transfer@7ef...(0xa29..., 0xef8..., 0x4ef2dcea863c9d0)   | Yes       |
| Transfer@df7...(0xef8..., 0x0, 0x18493fba64ef00000)      | Transfer@df7...(0xef8..., 0x0, 0x18493fba64ef00000)      | identical |
| Transfer@7ef...(0xdf7..., 0xef8..., 0x18493fba64ef00000) | Transfer@7ef...(0xdf7..., 0xef8..., 0x18493fba64ef00000) | identical |


# Reverted call contexts?

T_A reverse

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

Attacker EOA loss.