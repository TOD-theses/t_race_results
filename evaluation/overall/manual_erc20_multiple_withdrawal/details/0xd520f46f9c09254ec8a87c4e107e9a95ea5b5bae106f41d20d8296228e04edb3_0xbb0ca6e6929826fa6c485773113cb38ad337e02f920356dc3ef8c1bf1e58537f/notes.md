# TOD checker output

Transactions:
- T_A: [0xd520f46f9c09254ec8a87c4e107e9a95ea5b5bae106f41d20d8296228e04edb3](https://etherscan.io/tx/0xd520f46f9c09254ec8a87c4e107e9a95ea5b5bae106f41d20d8296228e04edb3)
- T_B: [0xbb0ca6e6929826fa6c485773113cb38ad337e02f920356dc3ef8c1bf1e58537f](https://etherscan.io/tx/0xbb0ca6e6929826fa6c485773113cb38ad337e02f920356dc3ef8c1bf1e58537f)


Attacker: [0x26ea744e5b887e5205727f55dfbe8685e3b21951](https://etherscan.io/address/0x26ea744e5b887e5205727f55dfbe8685e3b21951)
Victim: [0xb6c057591e073249f2d9d88ba59a46cfc9b59edb](https://etherscan.io/address/0xb6c057591e073249f2d9d88ba59a46cfc9b59edb)

Attacker gain tokens:
- ERC-20 [USDC](https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)

Victim loss tokens:
- ERC-20 [USDC](https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)

# Manually verified witness

T_A normal Transfer: Transfer(0xb6c..., 0x26e..., 0x9502f9000)
T_B normal Approval: Approval(0xb6c..., 0x26e..., 0xba448640a)
T_B reverse Approval: Approval(0xb6c..., 0x26e..., 0xba448640a)

# Transfer is the same in reverse scenario?

T_A reverse Transfer: Transfer(0xb6c..., 0x26e..., 0x9502f9000)

# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

T_A also has an Approval(0xb6c..., 0x26e..., 0x9502f9000) before the transfer.