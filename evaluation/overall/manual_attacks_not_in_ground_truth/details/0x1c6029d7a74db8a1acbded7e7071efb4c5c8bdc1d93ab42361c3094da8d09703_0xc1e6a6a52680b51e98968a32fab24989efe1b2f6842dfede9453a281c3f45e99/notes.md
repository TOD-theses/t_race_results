# TOD checker output

Transactions:
- T_A: [0x1c6029d7a74db8a1acbded7e7071efb4c5c8bdc1d93ab42361c3094da8d09703](https://etherscan.io/tx/0x1c6029d7a74db8a1acbded7e7071efb4c5c8bdc1d93ab42361c3094da8d09703)
- T_B: [0xc1e6a6a52680b51e98968a32fab24989efe1b2f6842dfede9453a281c3f45e99](https://etherscan.io/tx/0xc1e6a6a52680b51e98968a32fab24989efe1b2f6842dfede9453a281c3f45e99)


Attacker: [0x1542e790a742333ea6a2f171c5d07a2e7794eef4](https://etherscan.io/address/0x1542e790a742333ea6a2f171c5d07a2e7794eef4) (bot)
Victim: [0xa8ecbeaab5add9439fa544f4df2feda0b2d53cfa](https://etherscan.io/address/0xa8ecbeaab5add9439fa544f4df2feda0b2d53cfa)

Attacker gain tokens:
- ERC-20 [HBTC](https://etherscan.io/token/0x0316eb71485b0ab14103307bf65a021042c6d380)

Victim loss tokens:
- ERC-20 [HBTC](https://etherscan.io/token/0x0316eb71485b0ab14103307bf65a021042c6d380)

# Manually parsed logs

Containing attacker:

Traces for T_A are identical.

| Normal T_B                                      | Reverse T_B | Is gain? |
|-------------------------------------------------|-------------|----------|
| Transfer(0xa8e..., 0x154..., 0x3cd2231e3334c00) | <reverted>  | Yes      |

Containing victim:

Traces for T_A are identical.

| Normal T_B                                      | Reverse T_B | Is loss? |
|-------------------------------------------------|-------------|----------|
| Transfer(0xa8e..., 0x154..., 0x3cd2231e3334c00) | <reverted>  | Yes      |


# Reverted call contexts?

T_B reverse

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

The victim transaction has a value of 10 Ether. If we considered this, spending 10 Ether in the normal scenario vs 0 Ether in the (reverted) reverse scenario would fulfill the victim gain property.