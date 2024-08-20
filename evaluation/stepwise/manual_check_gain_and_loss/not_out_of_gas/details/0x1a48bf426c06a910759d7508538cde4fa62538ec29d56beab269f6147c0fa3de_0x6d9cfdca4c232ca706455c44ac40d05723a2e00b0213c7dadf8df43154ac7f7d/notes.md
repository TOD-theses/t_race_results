# TOD attack analysis

Transactions:
- T_A: [0x1a48bf426c06a910759d7508538cde4fa62538ec29d56beab269f6147c0fa3de](https://etherscan.io/tx/0x1a48bf426c06a910759d7508538cde4fa62538ec29d56beab269f6147c0fa3de)
- T_B: [0x6d9cfdca4c232ca706455c44ac40d05723a2e00b0213c7dadf8df43154ac7f7d](https://etherscan.io/tx/0x6d9cfdca4c232ca706455c44ac40d05723a2e00b0213c7dadf8df43154ac7f7d)

## Ground truth

### Attacker
Asset changes for: [0x5247cb423B36888c0aAdB915847f29306cf57cBa](https://etherscan.io/address/0x5247cb423B36888c0aAdB915847f29306cf57cBa)
- ERC20_TOKEN (+0x2c9b2dd5ae54ad) https://etherscan.io/token/0x83e6f1E41cdd28eAcEB20Cb649155049Fac3D5Aa


### Victim
Asset changes for: [0xF0EAf0C77c1362aD4dE668755be5559EB47cFB9f](https://etherscan.io/address/0xF0EAf0C77c1362aD4dE668755be5559EB47cFB9f)
- ERC20_TOKEN (-0xe1ecf6f2b049492fa) https://etherscan.io/token/0x4bD70556ae3F8a6eC6C4080A0C327B24325438f3


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: False
- attacker_bot_gain: False
- attacker_bot_loss: False
- victim_gain: True
- victim_loss: False

## Manually parsed logs

Containing attacker: (not parsed as our tool also reported attacker gain without loss)

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                                 | Reverse T_B                                                | Is loss?  |
|------------------------------------------------------------|------------------------------------------------------------|-----------|
| Transfer@dac...(0xf0e..., 0xd4a..., 0x77359400)            | Transfer@dac...(0xf0e..., 0xd4a..., 0x77359400)            | identical |
| Transfer@4bd...(0xd64..., 0xf0e..., 0x239858cc7b89e240cdc) | Transfer@4bd...(0xd64..., 0xf0e..., 0x2394b5272df80e7e013) | No        |



## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Yes

# First divergence

## T_B

SLOAD diverges at slot 0x8 (address 0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852, pc 3475):
- Normal: 5fb89ac2000000000000000049b1ca9895950000000021d3b542a33b45638739
- Reverse: 5fb89abe000000000000000049b59f409f3a0000000021d1f1d711d2790e2fff

This is written by T_A, therefore we overwrite it. However, the value written by T_A does not match the normal scenario value, hence an intermediary transaction also has written to this storage slot.


## Other notes

Victim gain for the ground truth tokens
