# TOD checker output

Transactions:
- T_A: [0xd48ad4bfa175ce421c5413fae1a1105c5e742f02ac8e5729943228e4cc09e7fa](https://etherscan.io/tx/0xd48ad4bfa175ce421c5413fae1a1105c5e742f02ac8e5729943228e4cc09e7fa)
- T_B: [0x113d461413ba53c909a6dbbcc5bf85dc975a2151e904671142721737de050d76](https://etherscan.io/tx/0x113d461413ba53c909a6dbbcc5bf85dc975a2151e904671142721737de050d76)


Attacker: [0x8f5adc58b32d4e5ca02eac0e293d35855999](https://etherscan.io/address/0x8f5adc58b32d4e5ca02eac0e293d35855999436c)
Victim: [0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50](https://etherscan.io/address/0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50)

Attacker gain tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

Victim loss tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

# Manually verified witness

T_A normal Transfer: Transfer(0x255..., 0x8f5..., 0x24d6e15cef5a2b994e2a)
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
