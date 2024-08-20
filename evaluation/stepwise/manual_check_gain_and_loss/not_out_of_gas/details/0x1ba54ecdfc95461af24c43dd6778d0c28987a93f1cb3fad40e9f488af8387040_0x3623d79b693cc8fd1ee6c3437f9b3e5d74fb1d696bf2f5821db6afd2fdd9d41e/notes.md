# TOD attack analysis

Transactions:
- T_A: [0x1ba54ecdfc95461af24c43dd6778d0c28987a93f1cb3fad40e9f488af8387040](https://etherscan.io/tx/0x1ba54ecdfc95461af24c43dd6778d0c28987a93f1cb3fad40e9f488af8387040)
- T_B: [0x3623d79b693cc8fd1ee6c3437f9b3e5d74fb1d696bf2f5821db6afd2fdd9d41e](https://etherscan.io/tx/0x3623d79b693cc8fd1ee6c3437f9b3e5d74fb1d696bf2f5821db6afd2fdd9d41e)

## Ground truth

### Attacker
Asset changes for: [0xe695594474Fc5e184c25f4E3312fD132FB9FBD13](https://etherscan.io/address/0xe695594474Fc5e184c25f4E3312fD132FB9FBD13)
- ETHER (+0x197f1ad8cff)


### Victim
Asset changes for: [0x5bCd2BC57ba7b6b073c352fC75Da9b01BF1B9fB6](https://etherscan.io/address/0x5bCd2BC57ba7b6b073c352fC75Da9b01BF1B9fB6)
- ERC20_TOKEN (-0x1a85b304c2991c) https://etherscan.io/token/0x610c67be018A5C5bdC70ACd8DC19688A11421073


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: False
- attacker_bot_gain: True
- attacker_bot_loss: False
- victim_gain: True
- victim_loss: False

## Manually parsed logs

Containing attacker: (not parsed as our tool also reported attacker gain without loss)

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                              | Reverse T_B                                             | Is loss?  |
|---------------------------------------------------------|---------------------------------------------------------|-----------|
| Transfer@a0b...(0x5bc..., 0xb4e..., 0x1dcd6500)         | Transfer@a0b...(0x5bc..., 0xb4e..., 0x1dcd6500)         | identical |
| Transfer@610...(0xcff..., 0x5bc..., 0x62bb1d22f79ce565) | Transfer@610...(0xcff..., 0x5bc..., 0x62b14ef9b7718bc9) | No        |



## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Yes

# First divergence

## T_B

SLOAD diverges at slot 0x8 (address 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, pc 3475):
- Normal: 5fb8b2140000000021101a31de65ed684bd2000000000000000048785621c1c0
- Reverse: 5fb8b20000000000210e743d74e0d131180e0000000000000000487bf0632abf

This is written by T_A, therefore we overwrite it. However, the value written by T_A does not match the normal scenario value, hence an intermediary transaction also has written to this storage slot.

## Other notes

Victim gain for the ground truth tokens.