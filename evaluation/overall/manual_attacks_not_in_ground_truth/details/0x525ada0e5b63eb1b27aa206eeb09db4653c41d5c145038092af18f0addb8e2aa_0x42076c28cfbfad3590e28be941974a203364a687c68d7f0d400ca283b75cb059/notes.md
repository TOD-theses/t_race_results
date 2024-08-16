# TOD checker output

Transactions:
- T_A: [0x525ada0e5b63eb1b27aa206eeb09db4653c41d5c145038092af18f0addb8e2aa](https://etherscan.io/tx/0x525ada0e5b63eb1b27aa206eeb09db4653c41d5c145038092af18f0addb8e2aa)
- T_B: [0x42076c28cfbfad3590e28be941974a203364a687c68d7f0d400ca283b75cb059](https://etherscan.io/tx/0x42076c28cfbfad3590e28be941974a203364a687c68d7f0d400ca283b75cb059)


Attacker: [0x7c5592fad8031e62318dabd81e2211e50a231ffb](https://etherscan.io/address/0x7c5592fad8031e62318dabd81e2211e50a231ffb) (bot)
Victim: [0x83e0e54ca1ea23a87b4b5938cbbed773d23ffd49](https://etherscan.io/address/0x83e0e54ca1ea23a87b4b5938cbbed773d23ffd49)

Attacker gain tokens:
- ERC-20 [SNP](https://etherscan.io/token/0x795dbf627484f8248d3d6c09c309825c1563e873)

Victim loss tokens:
- ERC-20 [SNP](https://etherscan.io/token/0x795dbf627484f8248d3d6c09c309825c1563e873)

# Manually parsed logs

Containing attacker:

| Normal T_A                                       | Reverse T_A                                      | Is gain?                  |
|--------------------------------------------------|--------------------------------------------------|---------------------------|
| Transfer(0x0, 0x7c5..., 0x21de06658ae908ea)      |                                                  | Yes (+0x21de06658ae908ea) |
| Transfer(0x7c5..., 0xe7e..., 0xc79cd889d842c800) | Transfer(0x7c5..., 0xe7e..., 0xc7a0aefc105de840) | Yes (+0x3d672381b2040)    |

| Normal T_B                                       | Reverse T_B                                      | Is gain?                 |
|--------------------------------------------------|--------------------------------------------------|--------------------------|
| Transfer(0x0, 0x7c5..., 0x36300a3c1174db0)       | Transfer(0x0, 0x7c5..., 0x254107094c00569c)      | No (-0x21de06658ae908ec) |
| Transfer(0x7c5..., 0x83e..., 0x1140c555fa826b00) | Transfer(0x7c5..., 0x83e..., 0x1140c6b2a640cd80) | Yes (+0x15cabbe6280)     |

Overall:
- attacker gains 0x3d7cee3d982be = 1081708516049598 SNP

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                       | Reverse T_B                                      | Is loss? |
|--------------------------------------------------|--------------------------------------------------|----------|
| Transfer(0x7c5..., 0x83e..., 0x1140c555fa826b00) | Transfer(0x7c5..., 0x83e..., 0x1140c6b2a640cd80) | Yes      |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

Attacker EOA loses SNP tokens, but we use the attacker bot here.