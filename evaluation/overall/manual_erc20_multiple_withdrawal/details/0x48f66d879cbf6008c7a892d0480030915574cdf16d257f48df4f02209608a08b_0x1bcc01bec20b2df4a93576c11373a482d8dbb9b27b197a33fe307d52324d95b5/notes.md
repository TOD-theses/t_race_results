# TOD checker output

Transactions:
- T_A: [0x48f66d879cbf6008c7a892d0480030915574cdf16d257f48df4f02209608a08b](https://etherscan.io/tx/0x48f66d879cbf6008c7a892d0480030915574cdf16d257f48df4f02209608a08b)
- T_B: [0x1bcc01bec20b2df4a93576c11373a482d8dbb9b27b197a33fe307d52324d95b5](https://etherscan.io/tx/0x1bcc01bec20b2df4a93576c11373a482d8dbb9b27b197a33fe307d52324d95b5)


Attacker: [0x8f5adc58b32d4e5ca02eac0e293d35855999436c](https://etherscan.io/address/0x8f5adc58b32d4e5ca02eac0e293d35855999436c)
Victim: [0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50](https://etherscan.io/address/0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50)

Attacker gain tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

Victim loss tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

# Manually verified witness

T_A normal Transfer: Transfer(0x255..., 0x8f5..., 0x24d368f8a1efa5158a6d)
T_B normal Approval: Approval(0x255..., 0x8f5..., 0x0)
T_B reverse Approval: Approval(0x255..., 0x8f5..., 0x0)

# Transfer is the same in reverse scenario?

T_A reverse Transfer: <reverted>

# Reverted call contexts?

T_A reverse

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

T_A also contains the same Approval. Thus, the attacker would have approved the tokens themselves. Also, the Approval witness has value 0, which does not allow an attack.
