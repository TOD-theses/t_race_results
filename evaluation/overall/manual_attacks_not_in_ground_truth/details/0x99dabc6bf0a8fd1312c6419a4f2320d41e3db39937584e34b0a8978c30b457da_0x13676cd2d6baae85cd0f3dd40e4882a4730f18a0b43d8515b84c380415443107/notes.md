# TOD checker output

Transactions:
- T_A: [0x99dabc6bf0a8fd1312c6419a4f2320d41e3db39937584e34b0a8978c30b457da](https://etherscan.io/tx/0x99dabc6bf0a8fd1312c6419a4f2320d41e3db39937584e34b0a8978c30b457da)
- T_B: [0x13676cd2d6baae85cd0f3dd40e4882a4730f18a0b43d8515b84c380415443107](https://etherscan.io/tx/0x13676cd2d6baae85cd0f3dd40e4882a4730f18a0b43d8515b84c380415443107)


Attacker: [0x8a31fe010489e7d49fdea09014ad925d12e70292](https://etherscan.io/address/0x8a31fe010489e7d49fdea09014ad925d12e70292)
Victim: [0xb8d2752c2f83a2149ab09d37daa8613f50b0ace1](https://etherscan.io/address/0xb8d2752c2f83a2149ab09d37daa8613f50b0ace1)

Attacker gain tokens:
- ERC-20 [kETH](https://etherscan.io/token/0xc4c43c78fb32f2c7f8417af5af3b85f090f1d327)

Victim loss tokens:
- ERC-20 [kETH](https://etherscan.io/token/0xc4c43c78fb32f2c7f8417af5af3b85f090f1d327)

# Manually parsed logs

Containing attacker:

| Normal T_A                                  | Reverse T_A                                 | Is gain? |
|---------------------------------------------|---------------------------------------------|----------|
| Transfer(0x0, 0x8a3..., 0x417592c37c3f0c62) | Transfer(0x0, 0x8a3..., 0x41759233eaf384cf) | Yes      |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                 | Reverse T_B                                | Is loss? |
|--------------------------------------------|--------------------------------------------|----------|
| Transfer(0x0, 0xb8d..., 0xd1783a3fbca49c4) | Transfer(0x0, 0xb8d..., 0xd1784339016b7c9) | Yes      |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes
