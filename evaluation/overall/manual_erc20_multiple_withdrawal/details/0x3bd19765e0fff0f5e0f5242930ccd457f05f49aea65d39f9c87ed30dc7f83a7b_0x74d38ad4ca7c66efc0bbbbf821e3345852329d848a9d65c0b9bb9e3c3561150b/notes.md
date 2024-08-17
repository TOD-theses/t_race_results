# TOD checker output

Transactions:
- T_A: [0x3bd19765e0fff0f5e0f5242930ccd457f05f49aea65d39f9c87ed30dc7f83a7b](https://etherscan.io/tx/0x3bd19765e0fff0f5e0f5242930ccd457f05f49aea65d39f9c87ed30dc7f83a7b)
- T_B: [0x74d38ad4ca7c66efc0bbbbf821e3345852329d848a9d65c0b9bb9e3c3561150b](https://etherscan.io/tx/0x74d38ad4ca7c66efc0bbbbf821e3345852329d848a9d65c0b9bb9e3c3561150b)


Attacker: [0xed5ad5f258eef6a9745042bde7d46e8a5254c183](https://etherscan.io/address/0xed5ad5f258eef6a9745042bde7d46e8a5254c183)
Victim: [0x3e66b66fd1d0b02fda6c811da9e0547970db2f21](https://etherscan.io/address/0x3e66b66fd1d0b02fda6c811da9e0547970db2f21)

Attacker gain tokens:
- ERC-20 [DUSD](https://etherscan.io/token/0x5bc25f649fc4e26069ddf4cf4010f9f706c23831)

Victim loss tokens:
- ERC-20 [DUSD](https://etherscan.io/token/0x5bc25f649fc4e26069ddf4cf4010f9f706c23831)

# Manually verified witness

T_A normal Transfer: Transfer(0x3e6..., 0xed5..., 0x18eee09b926e019393)
T_B normal Approval: Approval(0x3e6..., 0xed5..., 0x41601fa41fe900000)
T_B reverse Approval: Approval(0x3e6..., 0xed5..., 0x41601fa41fe900000)

# Transfer is the same in reverse scenario?

T_A reverse Transfer: Transfer(0x3e6..., 0xed5..., 0x18eee09b926e019393)

# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

T_A also contains the same Approval. Thus, the attacker would have approved the tokens themselves.
