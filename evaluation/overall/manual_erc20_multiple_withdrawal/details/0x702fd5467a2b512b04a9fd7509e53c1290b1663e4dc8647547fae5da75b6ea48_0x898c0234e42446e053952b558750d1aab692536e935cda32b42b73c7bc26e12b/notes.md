# TOD checker output

Transactions:
- T_A: [0x702fd5467a2b512b04a9fd7509e53c1290b1663e4dc8647547fae5da75b6ea48](https://etherscan.io/tx/0x702fd5467a2b512b04a9fd7509e53c1290b1663e4dc8647547fae5da75b6ea48)
- T_B: [0x898c0234e42446e053952b558750d1aab692536e935cda32b42b73c7bc26e12b](https://etherscan.io/tx/0x898c0234e42446e053952b558750d1aab692536e935cda32b42b73c7bc26e12b)


Attacker: [0x8f5adc58b32d4e5ca02eac0e293d35855999](https://etherscan.io/address/0x8f5adc58b32d4e5ca02eac0e293d35855999436c)
Victim: [0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50](https://etherscan.io/address/0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50)

Attacker gain tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

Victim loss tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

# Manually verified witness

T_A normal Transfer: Transfer(0x255..., 0x8f5..., 0x24d405a40238647a0a54)
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
