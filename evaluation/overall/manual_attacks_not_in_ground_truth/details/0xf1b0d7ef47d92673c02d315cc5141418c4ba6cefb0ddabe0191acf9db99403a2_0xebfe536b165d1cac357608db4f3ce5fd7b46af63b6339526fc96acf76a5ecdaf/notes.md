# TOD checker output

Transactions:
- T_A: [0xf1b0d7ef47d92673c02d315cc5141418c4ba6cefb0ddabe0191acf9db99403a2](https://etherscan.io/tx/0xf1b0d7ef47d92673c02d315cc5141418c4ba6cefb0ddabe0191acf9db99403a2)
- T_B: [0xebfe536b165d1cac357608db4f3ce5fd7b46af63b6339526fc96acf76a5ecdaf](https://etherscan.io/tx/0xebfe536b165d1cac357608db4f3ce5fd7b46af63b6339526fc96acf76a5ecdaf)


Attacker: [0xddc9ba421415daeaf56debe093af41bae002d527](https://etherscan.io/address/0xddc9ba421415daeaf56debe093af41bae002d527)
Victim: [0xd71f271ffa7a6580e5710feb7279d795a8272a66](https://etherscan.io/address/0xd71f271ffa7a6580e5710feb7279d795a8272a66)

Attacker gain tokens:
- ERC-20 [WBTC](https://etherscan.io/token/0x2260fac5e5542a773aa44fbcfedf7c193bc2c599)

Victim loss tokens:
- ERC-20 [WBTC](https://etherscan.io/token/0x2260fac5e5542a773aa44fbcfedf7c193bc2c599)

# Manually parsed logs

Containing attacker:

| Normal T_A                                      | Reverse T_A                                     | Is gain?  |
|-------------------------------------------------|-------------------------------------------------|-----------|
| Transfer(0xddc..., 0x514..., 0xcd5341243c98e31) | Transfer(0xddc..., 0x514..., 0xcd5341243c98e31) | identical |
| Transfer(0xbb2..., 0xddc..., 0x90a9e)           | Transfer(0xbb2..., 0xddc..., 0x90a16)           | Yes       |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                          | Reverse T_B                                         | Is loss?  |
|-----------------------------------------------------|-----------------------------------------------------|-----------|
| Transfer(0xd71..., 0xa47..., 0x23ea08cfecb04a00000) | Transfer(0xd71..., 0xa47..., 0x23ea08cfecb04a00000) | identical |
| Transfer(0xbb2..., 0xd71..., 0x36630ba)             | Transfer(0xbb2..., 0xd71..., 0x3663142)             | Yes       |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes
