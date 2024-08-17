# TOD checker output

Transactions:
- T_A: [0x89d5b49316f55a14514704dda830d603ff344e263609e4eb2ae0480dbb5b9524](https://etherscan.io/tx/0x89d5b49316f55a14514704dda830d603ff344e263609e4eb2ae0480dbb5b9524)
- T_B: [0x3080192048ffb806ed6fb53d1aa957ff59885858dc74d7f1c0994ec8e62dbaf8](https://etherscan.io/tx/0x3080192048ffb806ed6fb53d1aa957ff59885858dc74d7f1c0994ec8e62dbaf8)

# Manual check

| Normal T_B                                              | Reverse T_B                                             | Is TOD-Receiver? |
|---------------------------------------------------------|---------------------------------------------------------|------------------|
| CALL@0x5ac:7854(0x5ac..., 0x2ec..., 100000000000000000) | CALL@0x5ac:7854(0x2a7..., 0xc20..., 100000000000000000) | Yes              |

# Notes

T_A sets the storage slot 0xa0176eee3c5b559400de2e0f18609c2917e93ed5390da940f66b4bc11bf7ac12 to 0x2ecf9b31d34f72d5fa8587c77a4ec22e43d7722d, which is the address that receives the Ether in the normal scenario.
In the reverse scenario, T_B loads a different storage slot (0xac776ad71a36a5d200a92f2edcac32e9c4929c1711aed3c51b3da32260dd1756), containing a different address.

In both scenarios, the storage is loaded at pc 5779. I did not investigate the logic of the program, thus we do not know if this is a real attack. However, our TOD Receiver definition holds for this case.