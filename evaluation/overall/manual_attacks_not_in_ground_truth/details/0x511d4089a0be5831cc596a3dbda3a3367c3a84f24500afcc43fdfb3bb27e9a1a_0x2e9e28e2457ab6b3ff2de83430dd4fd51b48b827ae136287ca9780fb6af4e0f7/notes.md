# TOD checker output

Transactions:
- T_A: [0x511d4089a0be5831cc596a3dbda3a3367c3a84f24500afcc43fdfb3bb27e9a1a](https://etherscan.io/tx/0x511d4089a0be5831cc596a3dbda3a3367c3a84f24500afcc43fdfb3bb27e9a1a)
- T_B: [0x2e9e28e2457ab6b3ff2de83430dd4fd51b48b827ae136287ca9780fb6af4e0f7](https://etherscan.io/tx/0x2e9e28e2457ab6b3ff2de83430dd4fd51b48b827ae136287ca9780fb6af4e0f7)


Attacker: [0x7a250d5630b4cf539739df2c5dacb4c659f2488d](https://etherscan.io/address/0x7a250d5630b4cf539739df2c5dacb4c659f2488d) (bot)
Victim: [0x19f9b366d1b82d071ed9f65a01d35baa3f485cf4](https://etherscan.io/address/0x19f9b366d1b82d071ed9f65a01d35baa3f485cf4)

Attacker gain tokens:
- ERC-20 [WETH](https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)

Victim loss tokens:
- Ether

# Manually parsed logs

Containing attacker:

| Normal T_A                                      | Reverse T_A | Is gain?                 |
|-------------------------------------------------|-------------|--------------------------|
| CALL(0xc02..., 0x7a2..., 0xd109a96e3f6c738)     | <reverted>  | Yes (+0xd109a96e3f6c738) |
| CALL(0x7a2..., 0xc56..., 0xd109a96e3f6c738)     | <reverted>  | No (-0xd109a96e3f6c738)  |
| Transfer(0xe23..., 0x7a2..., 0xd109a96e3f6c738) | <reverted>  | Yes (+0xd109a96e3f6c738)                     |

| Normal T_B                                      | Reverse T_B                                     | Is gain? |
|-------------------------------------------------|-------------------------------------------------|----------|
| CALL(0xc02..., 0x7a2..., 0xe30e66d1767c9bb)     | CALL(0xc02..., 0x7a2..., 0xe52d43bc5dec743)     | Yes (+0xe30e66d1767c9bb)         |
| CALL(0x7a2..., 0x19f..., 0xe30e66d1767c9bb)     | CALL(0x7a2..., 0x19f..., 0xe52d43bc5dec743)     | No (-0xe30e66d1767c9bb)         |
| Transfer(0xe23..., 0x7a2..., 0xe30e66d1767c9bb) | Transfer(0xe23..., 0x7a2..., 0xe52d43bc5dec743) | No (-0x21edceae76fd88)         |

Overall:
- gains 0xceeacc8357fc9b0 = 931872148803275184 WETH


Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                         | Reverse T_B                                        | Is loss? |
|----------------------------------------------------|----------------------------------------------------|----------|
| Transfer(0x19f..., 0xe23..., 0x4761e49e5fb445b6f1) | Transfer(0x19f..., 0xe23..., 0x4761e49e5fb445b6f1) |          |
| CALL(0x7a2..., 0x19f..., 0xe30e66d1767c9bb)        | CALL(0x7a2..., 0x19f..., 0xe52d43bc5dec743)        |          |


# Reverted call contexts?

T_A reverse

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

The attacker EOA has a loss but the attacker bot has gain and no loss. Follows our definition, but does not make sense.

Also, there are two WETH withdrawals for the attacker bot, which is modelled by erebus but not in the definition.