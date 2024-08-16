# TOD checker output

Transactions:
- T_A: [0x0b935bffaa6df0cf7856856465ddb7aa5fde7b1650aad85e01d5c28afe264f06](https://etherscan.io/tx/0x0b935bffaa6df0cf7856856465ddb7aa5fde7b1650aad85e01d5c28afe264f06)
- T_B: [0xdad374bef0802f319700018a1568fc03f16aa0c1fad17c0f1c726ad161ecd70d](https://etherscan.io/tx/0xdad374bef0802f319700018a1568fc03f16aa0c1fad17c0f1c726ad161ecd70d)


Attacker: [0x2a70605e53a2a596e04df8a775e0e8c9fed62f9a](https://etherscan.io/address/0x2a70605e53a2a596e04df8a775e0e8c9fed62f9a) (bot)
Victim: [0xa0cb63e84cc64d6149051cad1a039ce76ec6aac6](https://etherscan.io/address/0xa0cb63e84cc64d6149051cad1a039ce76ec6aac6)

Attacker gain tokens:
- ERC-20 [TOM](https://etherscan.io/address/0xf7970499814654cd13cb7b6e7634a12a7a8a9abc)

Victim loss tokens:
- ERC-20 [TOM](https://etherscan.io/address/0xf7970499814654cd13cb7b6e7634a12a7a8a9abc)

# Manually parsed logs

Containing attacker:

| Normal T_A                                           | Reverse T_A                                          | Is gain? |
|------------------------------------------------------|------------------------------------------------------|----------|
| Transfer(0xb34..., 0x2a7..., 0xec5d537ee25fd175be01) | Transfer(0xb34..., 0x2a7..., 0xec5d537ee25fd175be01) | No       |

| Normal T_B                                    | Reverse T_B                                   | Is gain? |
|-----------------------------------------------|-----------------------------------------------|----------|
| Transfer(0x2a7..., 0xa0c..., 0x89ca39b479443) | Transfer(0x2a7..., 0xa0c..., 0x89e0da85d35db) | Yes      |

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                    | Reverse T_B                                   | Is loss? |
|-----------------------------------------------|-----------------------------------------------|----------|
| Transfer(0x2a7..., 0xa0c..., 0x89ca39b479443) | Transfer(0x2a7..., 0xa0c..., 0x89e0da85d35db) | Yes      |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

"Bot" seems like a normal smart contract.