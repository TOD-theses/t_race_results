# TOD checker output

Transactions:
- T_A: [0x4b80aa6fccf1aeacccc62273db904f1f7b53378ec33bebbb94352684464fc151](https://etherscan.io/tx/0x4b80aa6fccf1aeacccc62273db904f1f7b53378ec33bebbb94352684464fc151)
- T_B: [0xb8f0dbc18a04d95f16e5bcd4745946a297be5eb68f7f95993f10973b604a2b6d](https://etherscan.io/tx/0xb8f0dbc18a04d95f16e5bcd4745946a297be5eb68f7f95993f10973b604a2b6d)


Attacker: [0x89ea4b98dd4ff30bde3712378d37cad58b265eaf](https://etherscan.io/address/0x89ea4b98dd4ff30bde3712378d37cad58b265eaf)
Victim: [0x0ece7c1bfc9543b2cbea8f5577d02e5f59a9f176](https://etherscan.io/address/0x0ece7c1bfc9543b2cbea8f5577d02e5f59a9f176)

Attacker gain tokens:
- ERC-20 [CRV](https://etherscan.io/token/0xd533a949740bb3306d119cc777fa900ba034cd52)

Victim loss tokens:
- ERC-20 [CRV](https://etherscan.io/token/0xd533a949740bb3306d119cc777fa900ba034cd52)

# Manually parsed logs

Containing attacker:

| Normal T_A                                    | Reverse T_A | Is gain?       |
|-----------------------------------------------|-------------|----------------|
| Transfer(0x0, 0x89e..., 0x1cc0df5422dfb23d62) | <reverted>  | yes (reverted) |
| Transfer(0x0, 0x89e..., 0x185603f35631b8b1ff) | <reverted>  | yes (reverted) |
| Transfer(0x0, 0x89e..., 0x1267e65fc042d5e366) | <reverted>  | yes (reverted) |
| Transfer(0x0, 0x89e..., 0x141aa3d73ff15b7aef) | <reverted>  | yes (reverted) |
| Transfer(0x0, 0x89e..., 0xf107f947ce1291768)  | <reverted>  | yes (reverted) |
| Transfer(0x0, 0x89e..., 0xd8b88815442dfe4e3)  | <reverted>  | yes (reverted) |
| Transfer(0x0, 0x89e..., 0x12a2e283aa1d6ba1c8) | <reverted>  | Yes            |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|
|            |             |          |

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                   | Reverse T_B                                  | Is loss? |
|----------------------------------------------|----------------------------------------------|----------|
| Transfer(0x0, 0x0ec..., 0x3f70823737a2d8793) | Transfer(0x0, 0x0ec..., 0x3f708237c79f854d2) | Yes      |


# Reverted call contexts?

T_A reverse

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

Would be no attack if we considered transaction values, because T_A is reverted in the reverse scenario.