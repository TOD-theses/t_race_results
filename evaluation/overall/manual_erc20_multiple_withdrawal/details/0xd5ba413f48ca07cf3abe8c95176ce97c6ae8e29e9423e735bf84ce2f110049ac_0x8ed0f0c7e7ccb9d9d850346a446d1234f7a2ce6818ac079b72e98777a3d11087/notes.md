# TOD checker output

Transactions:
- T_A: [0xd5ba413f48ca07cf3abe8c95176ce97c6ae8e29e9423e735bf84ce2f110049ac](https://etherscan.io/tx/0xd5ba413f48ca07cf3abe8c95176ce97c6ae8e29e9423e735bf84ce2f110049ac)
- T_B: [0x8ed0f0c7e7ccb9d9d850346a446d1234f7a2ce6818ac079b72e98777a3d11087](https://etherscan.io/tx/0x8ed0f0c7e7ccb9d9d850346a446d1234f7a2ce6818ac079b72e98777a3d11087)


Attacker: [0x8f5adc58b32d4e5ca02eac0e293d35855999](https://etherscan.io/address/0x8f5adc58b32d4e5ca02eac0e293d35855999436c)
Victim: [0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50](https://etherscan.io/address/0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50)

Attacker gain tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

Victim loss tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

# Manually verified witness

T_A normal Transfer: Transfer(0x255..., 0x8f5..., 0x24ccec1dc0062af0bdfd)
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
