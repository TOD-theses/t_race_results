# TOD checker output

Transactions:
- T_A: [0xb37ad383ae9d3c87698ee2216c1cbc1a98e5f09527826d141016d5fe4634591c](https://etherscan.io/tx/0xb37ad383ae9d3c87698ee2216c1cbc1a98e5f09527826d141016d5fe4634591c)
- T_B: [0x6a55cbedeb4385f8dc5079bb0a69f220d9cd4dc1acc5461953b716ffb1c31053](https://etherscan.io/tx/0x6a55cbedeb4385f8dc5079bb0a69f220d9cd4dc1acc5461953b716ffb1c31053)


Attacker: [0xd6ad7a6750a7593e092a9b218d66c0a814a3436e](https://etherscan.io/address/0xd6ad7a6750a7593e092a9b218d66c0a814a3436e)
Victim: [0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3](https://etherscan.io/address/0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3)

Attacker gain tokens:
- ERC-20 [USDC](https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)

Victim loss tokens:
- ERC-20 [USDC](https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)

# Manually verified witness

T_A normal Transfer: Transfer(0xbbc..., 0xd6a..., 0xa418e83a)
T_B normal Approval: Approval(0xbbc..., 0xd6a..., 0xe41a9e591)
T_B reverse Approval: Approval(0xbbc..., 0xd6a..., 0xe41a9e591)

# Transfer is the same in reverse scenario?

T_A reverse Transfer: Transfer(0xbbc..., 0xd6a..., 0xa418e83a)

# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

T_A also contains the same Approval. Thus, the attacker would have approved the tokens themselves.