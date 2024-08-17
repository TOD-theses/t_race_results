# TOD checker output

Transactions:
- T_A: [0xefbcd4f5916c18cd546d77b5785695d5d5623c8e7122fc3e5c5bd84a4a3a93c8](https://etherscan.io/tx/0xefbcd4f5916c18cd546d77b5785695d5d5623c8e7122fc3e5c5bd84a4a3a93c8)
- T_B: [0x8d8b72676827fec48e5399a06f753ce7203ffeb2fbc59a451e7b9c6782467371](https://etherscan.io/tx/0x8d8b72676827fec48e5399a06f753ce7203ffeb2fbc59a451e7b9c6782467371)


Attacker: [0x8f5adc58b32d4e5ca02eac0e293d35855999](https://etherscan.io/address/0x8f5adc58b32d4e5ca02eac0e293d35855999436c)
Victim: [0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50](https://etherscan.io/address/0x25550cccbd68533fa04bfd3e3ac4d09f9e00fc50)

Attacker gain tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

Victim loss tokens:
- ERC-20 [FARM](https://etherscan.io/token/0xa0246c9032bc3a600820415ae600c6388619a14d)

# Manually verified witness

T_A normal Transfer: Transfer(0x255..., 0x8f5..., 0x24d37e48058a78137d1e)
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
