# TOD checker output

Transactions:
- T_A: [0xcd57b12667f9d354c2826b296e9c7c017e1a26731e8c2d41533eb4565939f9aa](https://etherscan.io/tx/0xcd57b12667f9d354c2826b296e9c7c017e1a26731e8c2d41533eb4565939f9aa)
- T_B: [0x8f2954d802dd9261a50946bc84b6e3d8fa682bc868e51749b5f4067d9f6e60cd](https://etherscan.io/tx/0x8f2954d802dd9261a50946bc84b6e3d8fa682bc868e51749b5f4067d9f6e60cd)


Attacker: [0xfae2809935233d4bfe8a56c2355c4a2e7d1fff1a](https://etherscan.io/address/0xfae2809935233d4bfe8a56c2355c4a2e7d1fff1a)
Victim: [0x3e66b66fd1d0b02fda6c811da9e0547970db2f21](https://etherscan.io/address/0x3e66b66fd1d0b02fda6c811da9e0547970db2f21)

Attacker gain tokens:
- ERC-20 [DOUGH](https://etherscan.io/token/0xad32a8e6220741182940c5abf610bde99e737b2d)

Victim loss tokens:
- ERC-20 [DOUGH](https://etherscan.io/token/0xad32a8e6220741182940c5abf610bde99e737b2d)

# Manually verified witness

T_A normal Transfer: Transfer(0x3e6..., 0xfae..., 0x6c6b935b8bbd40000)
T_B normal Approval: Approval(0x3e6..., 0xfae..., 0x39c500dbe42ec60000)
T_B reverse Approval: Approval(0x3e6..., 0xfae..., 0x39c500dbe42ec60000)

# Transfer is the same in reverse scenario?

T_A reverse Transfer: <reverted>

# Reverted call contexts?

T_A reverse

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

T_A also contains the same Approval. Thus, the attacker would have approved the tokens themselves.
