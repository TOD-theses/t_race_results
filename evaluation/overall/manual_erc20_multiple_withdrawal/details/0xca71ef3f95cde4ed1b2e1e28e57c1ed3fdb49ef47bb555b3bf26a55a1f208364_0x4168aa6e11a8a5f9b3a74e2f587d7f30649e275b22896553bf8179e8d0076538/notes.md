# TOD checker output

Transactions:
- T_A: [0xca71ef3f95cde4ed1b2e1e28e57c1ed3fdb49ef47bb555b3bf26a55a1f208364](https://etherscan.io/tx/0xca71ef3f95cde4ed1b2e1e28e57c1ed3fdb49ef47bb555b3bf26a55a1f208364)
- T_B: [0x4168aa6e11a8a5f9b3a74e2f587d7f30649e275b22896553bf8179e8d0076538](https://etherscan.io/tx/0x4168aa6e11a8a5f9b3a74e2f587d7f30649e275b22896553bf8179e8d0076538)


Attacker: [0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51](https://etherscan.io/address/0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
Victim: [0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3](https://etherscan.io/address/0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3)

Attacker gain tokens:
- ERC-20 [yDAI](https://etherscan.io/token/0x16de59092dae5ccf4a1e6439d611fd0653f0bd01)

Victim loss tokens:
- ERC-20 [yDAI](https://etherscan.io/token/0x16de59092dae5ccf4a1e6439d611fd0653f0bd01)

# Manually verified witness

T_A normal Transfer: Transfer(0xbbc..., 0x45f..., 0x0)
T_B normal Approval: Approval(0xbbc..., 0x45f..., 0x81125db1777cb012f4)
T_B reverse Approval: Approval(0xbbc..., 0x45f..., 0x81125db1777cb012f4)

# Transfer is the same in reverse scenario?

T_A reverse Transfer: Transfer(0xbbc..., 0x45f..., 0x0)

# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

Zero value Transfer is no attack.