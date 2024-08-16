# TOD checker output

Transactions:
- T_A: [0xadb38851b454b1a7ad5f61ef3742143b1b07a29bc054b1b0b48df4ed01c78318](https://etherscan.io/tx/0xadb38851b454b1a7ad5f61ef3742143b1b07a29bc054b1b0b48df4ed01c78318)
- T_B: [0x38662438615629b9fa8ac70667a9083d1fbb0103eebb717109c795944796bb3f](https://etherscan.io/tx/0x38662438615629b9fa8ac70667a9083d1fbb0103eebb717109c795944796bb3f)


Attacker: [0x5b82b3da49a6a7b5eea8f1b5d3c35766af614cf0](https://etherscan.io/address/0x5b82b3da49a6a7b5eea8f1b5d3c35766af614cf0) (bot)
Victim: [0xdbd86b07ca22ad8d0a1cd883c61f9068cb6c415b](https://etherscan.io/address/0xdbd86b07ca22ad8d0a1cd883c61f9068cb6c415b)

Attacker gain tokens:
- ERC-20 [VOX](https://etherscan.io/token/0x12d102f06da35cc0111eb58017fd2cd28537d0e1)

Victim loss tokens:
- ERC-20 [VOX](https://etherscan.io/token/0x12d102f06da35cc0111eb58017fd2cd28537d0e1)

# Manually parsed logs

Containing attacker:

| Normal T_A                                     | Reverse T_A                                    | Is gain?                 |
|------------------------------------------------|------------------------------------------------|--------------------------|
| Transfer(0x0, 0x5b8..., 0x349a8faac51e400)     |                                                | Yes (+0x349a8faac51e400) |
| Transfer(0x5b8..., 0x3b3..., 0x8f795423961fb5) | Transfer(0x5b8..., 0x3b3..., 0x8f7a684b5e5760) | Yes (+0x11427c837ab)     |

| Normal T_B                                     | Reverse T_B                                    | Is gain?                |
|------------------------------------------------|------------------------------------------------|-------------------------|
| Transfer(0x0, 0x5b8..., 0xb1310c5a2c300)       | Transfer(0x0, 0x5b8..., 0x354bc0b71f4a700)     | No (-0x349a8faac51e400) |
| Transfer(0x5b8..., 0xdbd..., 0x4d6b2b37f27693) | Transfer(0x5b8..., 0xdbd..., 0x4d6b2b37f332bf) | Yes (+0xbc2c)           |

Overall:
- attacker gains 0x11427c8f3d7 = 1186078454743 VOX

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                     | Reverse T_B                                    | Is loss? |
|------------------------------------------------|------------------------------------------------|----------|
| Transfer(0x5b8..., 0xdbd..., 0x4d6b2b37f27693) | Transfer(0x5b8..., 0xdbd..., 0x4d6b2b37f332bf) | Yes      |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

Attacker EOA loss