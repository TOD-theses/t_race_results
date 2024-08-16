# TOD checker output

Transactions:
- T_A: [0xa6f2e1def6e98e26bdca4e80d7b486f255444d2000edd7c84610f88f302f2d24](https://etherscan.io/tx/0xa6f2e1def6e98e26bdca4e80d7b486f255444d2000edd7c84610f88f302f2d24)
- T_B: [0x5e32e28f2fe834c84e61ba67f29f8785bb160136560577d6879bc12225143378](https://etherscan.io/tx/0x5e32e28f2fe834c84e61ba67f29f8785bb160136560577d6879bc12225143378)


Attacker: [0xa823ffc769162e7a152cbdaa383909b6d0d1d14f](https://etherscan.io/address/0xa823ffc769162e7a152cbdaa383909b6d0d1d14f)
Victim: [0x1f28c6fb3ea8ba23038c70a51d8986c5d1276a8d](https://etherscan.io/address/0x1f28c6fb3ea8ba23038c70a51d8986c5d1276a8d)

Attacker gain tokens:
- ERC-20 [MINDS](https://etherscan.io/token/0xb26631c6dda06ad89b93c71400d25692de89c068)

Victim loss tokens:
- ERC-20 [MINDS](https://etherscan.io/token/0xb26631c6dda06ad89b93c71400d25692de89c068)

# Manually parsed logs

Containing attacker:

| Normal T_A                                  | Reverse T_A                                 | Is gain?  |
|---------------------------------------------|---------------------------------------------|-----------|

| Normal T_B                                        | Reverse T_B | Is gain? |
|---------------------------------------------------|-------------|----------|
| Transfer(0x1f2..., 0xa82..., 0x1158e460913cffdbc) | <reverted>  | Yes      |

Containing victim:

| Normal T_A                                  | Reverse T_A                                 | Is loss?  |
|---------------------------------------------|---------------------------------------------|-----------|
| CALL(0x361..., 0x1f2..., 0x1ac09acc70f21ea) | CALL(0x361..., 0x1f2..., 0x1ac09acc70f21ea) | identical |

| Normal T_B                                        | Reverse T_B | Is loss? |
|---------------------------------------------------|-------------|----------|
| Transfer(0x1f2..., 0xa82..., 0x1158e460913cffdbc) | <reverted>  | Yes      |


# Reverted call contexts?

T_B reverse

# Normal scenario logs match Etherscan logs?



# Other notes
