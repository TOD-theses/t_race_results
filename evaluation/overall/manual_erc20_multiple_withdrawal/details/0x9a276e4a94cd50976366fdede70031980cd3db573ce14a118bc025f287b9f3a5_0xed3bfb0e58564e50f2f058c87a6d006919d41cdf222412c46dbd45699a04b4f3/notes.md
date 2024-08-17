# TOD checker output

Transactions:
- T_A: [0x9a276e4a94cd50976366fdede70031980cd3db573ce14a118bc025f287b9f3a5](https://etherscan.io/tx/0x9a276e4a94cd50976366fdede70031980cd3db573ce14a118bc025f287b9f3a5)
- T_B: [0xed3bfb0e58564e50f2f058c87a6d006919d41cdf222412c46dbd45699a04b4f3](https://etherscan.io/tx/0xed3bfb0e58564e50f2f058c87a6d006919d41cdf222412c46dbd45699a04b4f3)


Attacker: [0x04bc0ab673d88ae9dbc9da2380cb6b79c4bca9ae](https://etherscan.io/address/0x04bc0ab673d88ae9dbc9da2380cb6b79c4bca9ae)
Victim: [0x79a8c46dea5ada233abaffd40f3a0a2b1e5a4f27](https://etherscan.io/address/0x79a8c46dea5ada233abaffd40f3a0a2b1e5a4f27)

Attacker gain tokens:
- ERC-20 [BUSD](https://etherscan.io/token/0x4fabb145d64652a948d72533023f6e7a623c7c53)

Victim loss tokens:
- ERC-20 [BUSD](https://etherscan.io/token/0x4fabb145d64652a948d72533023f6e7a623c7c53)

# Manually verified witness

T_A normal Transfer: Transfer(0x79a..., 0x4bc..., 0x504a69b7f2dee602c0)
T_B normal Approval: Approval(0x79a..., 0x4bc..., 0x3120bec57b51c100000)
T_B reverse Approval: Approval(0x79a..., 0x4bc..., 0x3120bec57b51c100000)

# Transfer is the same in reverse scenario?

T_A reverse Transfer: Transfer(0x78a..., 0x4bc..., 0x504a69b7f2dee602c0)

# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

T_A also contains the same Approval. Thus, the attacker would have approved the tokens themselves.