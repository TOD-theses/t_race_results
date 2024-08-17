# TOD checker output

Transactions:
- T_A: [0xda3b82043ced9cd9faf31bd83a67958e9e3081be5faa63b623dc6e56578c7891](https://etherscan.io/tx/0xda3b82043ced9cd9faf31bd83a67958e9e3081be5faa63b623dc6e56578c7891)
- T_B: [0xbcbd871c71deb7e59e5df5ad8e062b9f649bbcb3cef0694d18932ffbca1c5c0e](https://etherscan.io/tx/0xbcbd871c71deb7e59e5df5ad8e062b9f649bbcb3cef0694d18932ffbca1c5c0e)


Attacker: [0x8f5adc58b32d4e5ca02eac0e293d35855999](https://etherscan.io/address/0x8f5adc58b32d4e5ca02eac0e293d35855999436c)
Victim: [0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50](https://etherscan.io/address/0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50)

Attacker gain tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

Victim loss tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

# Manually verified witness

T_A normal Transfer: Transfer(0x255..., 0x8f5..., 0x24ce113b84b51f477f09)
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
