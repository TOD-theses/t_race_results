# TOD attack analysis

Transactions:
- T_A: [0x9ad045d254834a0e4db8cf22ae366b234f657c9b65c8b79a01cc55fb2428b55b](https://etherscan.io/tx/0x9ad045d254834a0e4db8cf22ae366b234f657c9b65c8b79a01cc55fb2428b55b)
- T_B: [0x1b221fb18b23b81dd32075172e19c467e33f1cd08d2f312c1671ebac5e1aadf5](https://etherscan.io/tx/0x1b221fb18b23b81dd32075172e19c467e33f1cd08d2f312c1671ebac5e1aadf5)

## Ground truth

### Attacker
Asset changes for: [0x20B13507f942071B4B245Be88D2053013efbbCBA](https://etherscan.io/address/0x20B13507f942071B4B245Be88D2053013efbbCBA)
- ERC20_TOKEN (+0x1036ebfb9f974) https://etherscan.io/token/0x8888801aF4d980682e47f1A9036e589479e835C5


### Victim
Asset changes for: [0x14B005380e4755F9963fD02fDe99896Cf02160AB](https://etherscan.io/address/0x14B005380e4755F9963fD02fDe99896Cf02160AB)
- ERC20_TOKEN (-0x37cd2d6e5c19b3) https://etherscan.io/token/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: False
- attacker_eoa_loss: False
- attacker_bot_gain: False
- attacker_bot_loss: False
- victim_gain: True
- victim_loss: True

## Manually parsed logs

Not parsed, as T_A traces are identical in normal and reverse scenario, which is the reason we do not have attacker gain.

## Reverted call contexts?

T_B reverse

## Normal scenario logs match Etherscan logs?

Not checked

## First divergence (T_B)

SLOAD diverges at slot 0x8 (address 0x4d96369002fc5b9687ee924d458a7e5baa5df34e, pc 3475)
- Normal: 5fb88b1400000000007e24517c538be0c0150000000003ea107223c520a8d223
- Reverse: 5fb88aee00000000007de0c2bf41f1ec06970000000003ec22490e7485c1e366

This is written by T_A, therefore we overwrite it. However, the value written by T_A does not match the normal scenario value, hence an intermediary transaction also has written to this storage slot.


## Partial overwrites

We overwrite the state of T_B with Delta_T_A for the reverse scenario. Thus, all the state changes by T_A are reverted to the prestate of T_A.

For two intermediary transactions, reverting the changes of T_A also reverts following changes of the intermediary transaction:
For 0x7c9b117a66acba009ad734507f08cdb07f2241339c6a5e947d4a4afdbf8c8a38:
- storage@0x4d96369002fc5b9687ee924d458a7e5baa5df34e@0x0000000000000000000000000000000000000000000000000000000000000008
- storage@0x8888801af4d980682e47f1a9036e589479e835c5@0xbba30aa71f0946f41bdea4d6bf4e956e5c5dd7778c8ed70f1721a093bb7be698
- storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0x64e8de5880dcd860292f919bddc0fdf9ede41c0e0a2fdefd99b32c9b41381896

For 0x8a0f1557a06bf3367681dff765bf9906da98129927ff17a82d0c5cbdd1230034:
- storage@0x4d96369002fc5b9687ee924d458a7e5baa5df34e@0x0000000000000000000000000000000000000000000000000000000000000008
- storage@0x8888801af4d980682e47f1a9036e589479e835c5@0xbba30aa71f0946f41bdea4d6bf4e956e5c5dd7778c8ed70f1721a093bb7be698
- storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0x64e8de5880dcd860292f919bddc0fdf9ede41c0e0a2fdefd99b32c9b4138189

However, it does not revert the following changes which are also accessed by T_B:
For 0x7c9b117a66acba009ad734507f08cdb07f2241339c6a5e947d4a4afdbf8c8a38:
- storage@0x4d96369002fc5b9687ee924d458a7e5baa5df34e@0x000000000000000000000000000000000000000000000000000000000000000a
- storage@0x4d96369002fc5b9687ee924d458a7e5baa5df34e@0x0000000000000000000000000000000000000000000000000000000000000009

For 0x8a0f1557a06bf3367681dff765bf9906da98129927ff17a82d0c5cbdd1230034:
- storage@0x8888801af4d980682e47f1a9036e589479e835c5@0x7718372ae9b89f6e2a891d72f64f8d7bfe32f5b677ae8b4a6a3b2594fc712182
- storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0x9c6c36ad38b084cbef50f8da801749f3e2fb41bbc473394ee0dd2d543a7d851a

As such, the changes by this intermediary transaction are partially kept.

tod_checker outputs that T_A is TOD with both intermediary transactions and both intermediary transactions are TOD with T_B.

## Other notes

T_B reverts in the reverse scenario (i.e. makes no state changes except for the gas costs), thus the traces for T_A are the same (before T_B and after the reverted T_B reverse).
