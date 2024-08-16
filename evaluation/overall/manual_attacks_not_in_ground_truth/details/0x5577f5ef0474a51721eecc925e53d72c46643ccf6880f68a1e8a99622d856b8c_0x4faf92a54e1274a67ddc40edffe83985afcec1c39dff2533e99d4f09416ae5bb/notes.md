# TOD checker output

Transactions:
- T_A: [0x5577f5ef0474a51721eecc925e53d72c46643ccf6880f68a1e8a99622d856b8c](https://etherscan.io/tx/0x5577f5ef0474a51721eecc925e53d72c46643ccf6880f68a1e8a99622d856b8c)
- T_B: [0x4faf92a54e1274a67ddc40edffe83985afcec1c39dff2533e99d4f09416ae5bb](https://etherscan.io/tx/0x4faf92a54e1274a67ddc40edffe83985afcec1c39dff2533e99d4f09416ae5bb)


Attacker: [0x5b82b3da49a6a7b5eea8f1b5d3c35766af614cf0](https://etherscan.io/address/0x5b82b3da49a6a7b5eea8f1b5d3c35766af614cf0) (bot)
Victim: [0xef192a605f92dcf72726318607c5891f455857cd](https://etherscan.io/address/0xef192a605f92dcf72726318607c5891f455857cd)

Attacker gain tokens:
- ERC-20 [VOX](https://etherscan.io/token/0x12d102f06da35cc0111eb58017fd2cd28537d0e1)

Victim loss tokens:
- ERC-20 [VOX](https://etherscan.io/token/0x12d102f06da35cc0111eb58017fd2cd28537d0e1)

# Manually parsed logs

Containing attacker:

| Normal T_A                                      | Reverse T_A                                     | Is gain?  |
|-------------------------------------------------|-------------------------------------------------|-----------|
| Transfer(0x0, 0x5b8..., 0x427264a1d092000)      | Transfer(0x0, 0x5b8..., 0x427264a1d092000)      | identical |
| Transfer(0x2ed..., 0x5b8..., 0x15b1a7c0fdde316) | Transfer(0x2ed..., 0x5b8..., 0x15b1a7c0fdde316) | identical |

| Normal T_B                                    | Reverse T_B                                | Is gain?  |
|-----------------------------------------------|--------------------------------------------|-----------|
| Transfer(0x0, 0x5b8..., 0x570383c7b5b300)     | Transfer(0x0, 0x5b8..., 0x570383c7b5b300)  | identical |
| Transfer(0x5b8..., 0xef1..., 0xa0cfd5466e41a) | Transfer(0x5b8, 0xef1..., 0xa0cfd5cee0ad5) | Yes       |

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                    | Reverse T_B                | Is loss? |
|-----------------------------------------------|----------------------------|----------|
| Transfer(0x5b8..., 0xef1..., 0xa0cfd5466e41a) | Transfer(0x5b8, 0xef1...,) | Yes      |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

Bot doesn't look like a bot.