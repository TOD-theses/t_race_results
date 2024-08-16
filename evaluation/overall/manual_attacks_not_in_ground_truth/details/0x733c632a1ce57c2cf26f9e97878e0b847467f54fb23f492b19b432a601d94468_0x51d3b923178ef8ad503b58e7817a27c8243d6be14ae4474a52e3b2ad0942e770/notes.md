# TOD checker output

Transactions:
- T_A: [0x733c632a1ce57c2cf26f9e97878e0b847467f54fb23f492b19b432a601d94468](https://etherscan.io/tx/0x733c632a1ce57c2cf26f9e97878e0b847467f54fb23f492b19b432a601d94468)
- T_B: [0x51d3b923178ef8ad503b58e7817a27c8243d6be14ae4474a52e3b2ad0942e770](https://etherscan.io/tx/0x51d3b923178ef8ad503b58e7817a27c8243d6be14ae4474a52e3b2ad0942e770)


Attacker: [0x8e678b655a6b6e7f31747557a6a90a529b67a990](https://etherscan.io/address/0x8e678b655a6b6e7f31747557a6a90a529b67a990) (bot)
Victim: [0x493446f46b8c67ef26ab133790ee5c980cdbbde4](https://etherscan.io/address/0x493446f46b8c67ef26ab133790ee5c980cdbbde4)

Attacker gain tokens:
- ERC-20 [SFR](https://etherscan.io/token/0x8ab98c28295ea3bd2db6ac8b3ca57a625c054bd1)

Victim loss tokens:
- ERC-20 [SFR](https://etherscan.io/token/0x8ab98c28295ea3bd2db6ac8b3ca57a625c054bd1)

# Manually parsed logs

Containing attacker:

| Normal T_A                                       | Reverse T_A                                      | Is gain?                 |
|--------------------------------------------------|--------------------------------------------------|--------------------------|
| Transfer(0x0, 0x8e6..., 0x146a96a0e9f31d8)       |                                                  | Yes (+0x146a96a0e9f31d8) |
| Transfer(0x200..., 0x8e6..., 0x576c03e2f942385d) | Transfer(0x200..., 0x8e6..., 0x576c03e2f942385d) | identical                |

| Normal T_B                                     | Reverse T_B                                    | Is gain?                |
|------------------------------------------------|------------------------------------------------|-------------------------|
| Transfer(0x0, 0x8e6..., 0x1337245b368a75)      | Transfer(0x0, 0x8e6..., 0x159e08e69d5bc4e)     | No (-0x146a96a0e9f31d9) |
| Transfer(0x8e6..., 0x493..., 0xbf67837fb39c15) | Transfer(0x8e6..., 0x493..., 0xbf678832a21bb7) | Yes (+0x4b2ee7fa2)      |

Overall:
- attacker gains 0x4b2ee7fa1 = 20181843873 SFR

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                     | Reverse T_B                                    | Is loss? |
|------------------------------------------------|------------------------------------------------|----------|
| Transfer(0x8e6..., 0x493..., 0xbf67837fb39c15) | Transfer(0x8e6..., 0x493..., 0xbf678832a21bb7) | Yes      |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes
