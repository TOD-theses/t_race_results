# TOD checker output

Transactions:
- T_A: [0x113d461413ba53c909a6dbbcc5bf85dc975a2151e904671142721737de050d76](https://etherscan.io/tx/0x113d461413ba53c909a6dbbcc5bf85dc975a2151e904671142721737de050d76)
- T_B: [0x6fdefd342efbaec48e0b8b2e21979b3447d8ef5b3ebfd2b909b394194e79f659](https://etherscan.io/tx/0x6fdefd342efbaec48e0b8b2e21979b3447d8ef5b3ebfd2b909b394194e79f659)


Attacker: [0x8f5adc58b32d4e5ca02eac0e293d35855999436c](https://etherscan.io/address/0x8f5adc58b32d4e5ca02eac0e293d35855999436c)
Victim: [0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50](https://etherscan.io/address/0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50)

Attacker gain tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

Victim loss tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

# Manually verified witness

T_A normal Transfer: Transfer(0x255..., 0x8f5..., 0x24d6ec4748c6914c6a36)
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