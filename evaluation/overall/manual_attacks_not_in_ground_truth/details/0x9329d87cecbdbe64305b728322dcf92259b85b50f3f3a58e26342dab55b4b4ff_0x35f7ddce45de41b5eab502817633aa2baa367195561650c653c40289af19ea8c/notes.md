# TOD checker output

Transactions:
- T_A: [0x9329d87cecbdbe64305b728322dcf92259b85b50f3f3a58e26342dab55b4b4ff](https://etherscan.io/tx/0x9329d87cecbdbe64305b728322dcf92259b85b50f3f3a58e26342dab55b4b4ff)
- T_B: [0x35f7ddce45de41b5eab502817633aa2baa367195561650c653c40289af19ea8c](https://etherscan.io/tx/0x35f7ddce45de41b5eab502817633aa2baa367195561650c653c40289af19ea8c)


Attacker: [0xcc50953a743b9ce382f423e37b07efa6f9d9b000](https://etherscan.io/address/0xcc50953a743b9ce382f423e37b07efa6f9d9b000)
Victim: [0x7cc0540ca8270e03318a74f0c3643522e7561f5f](https://etherscan.io/address/0x7cc0540ca8270e03318a74f0c3643522e7561f5f)

Attacker gain tokens:
- ERC-20 [ICHI](https://etherscan.io/token/0x903bef1736cddf2a537176cf3c64579c3867a881)

Victim loss tokens:
- ERC-20 [ICHI](https://etherscan.io/token/0x903bef1736cddf2a537176cf3c64579c3867a881)

# Manually parsed logs

Containing attacker:

| Normal T_A                                | Reverse T_A                               | Is gain?  |
|-------------------------------------------|-------------------------------------------|-----------|
| Transfer(0xcc5..., 0x8fe..., 0x2bca72256) | Transfer(0xcc5..., 0x8fe..., 0x2bcd98370) | Yes       |
| Transfer(0xcc5..., 0x8fe..., 0x378bf71ab) | Transfer(0xcc5..., 0x8fe..., 0x378bf71ab) | identical |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                 | Reverse T_B                                | Is loss?  |
|--------------------------------------------|--------------------------------------------|-----------|
| Transfer(0xcc5..., 0x7cc..., 0x53d0cbfcd2) | Transfer(0xcc5..., 0x7cc..., 0x53d2402353) | Yes       |
| Transfer(0xcc5..., 0x7cc..., 0xa969798ff)  | Transfer(0xcc5..., 0x7cc..., 0xa969798ff)  | identical |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

Attacker EOA has losses.