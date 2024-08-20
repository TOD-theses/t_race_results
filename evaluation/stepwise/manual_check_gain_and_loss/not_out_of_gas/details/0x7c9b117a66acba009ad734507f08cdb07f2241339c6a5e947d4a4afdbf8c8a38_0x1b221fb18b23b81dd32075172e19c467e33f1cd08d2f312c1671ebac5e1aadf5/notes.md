# TOD attack analysis

Transactions:
- T_A: [0x7c9b117a66acba009ad734507f08cdb07f2241339c6a5e947d4a4afdbf8c8a38](https://etherscan.io/tx/0x7c9b117a66acba009ad734507f08cdb07f2241339c6a5e947d4a4afdbf8c8a38)
- T_B: [0x1b221fb18b23b81dd32075172e19c467e33f1cd08d2f312c1671ebac5e1aadf5](https://etherscan.io/tx/0x1b221fb18b23b81dd32075172e19c467e33f1cd08d2f312c1671ebac5e1aadf5)

## Ground truth

### Attacker
Asset changes for: [0x39b3363948888e3e73a701714ffAf746041c71C7](https://etherscan.io/address/0x39b3363948888e3e73a701714ffAf746041c71C7)
- ERC20_TOKEN (+0x1b5382f7e940) https://etherscan.io/token/0x8888801aF4d980682e47f1A9036e589479e835C5


### Victim
Asset changes for: [0x14B005380e4755F9963fD02fDe99896Cf02160AB](https://etherscan.io/address/0x14B005380e4755F9963fD02fDe99896Cf02160AB)
- ERC20_TOKEN (-0x624f42e905bd70) https://etherscan.io/token/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: False
- attacker_eoa_loss: True
- attacker_bot_gain: False
- attacker_bot_loss: False
- victim_gain: True
- victim_loss: False

## Manually parsed logs

Containing attacker:

| Normal T_A                                              | Reverse T_A                                             | Is gain? |
|---------------------------------------------------------|---------------------------------------------------------|----------|
| Transfer@888...(0x4d9..., 0x39b..., 0x1609519b2647289a) | Transfer@888...(0x4d9..., 0x39b..., 0x162cd9c5a28a4792) | No       |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim (not investigated)


## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Yes

## First divergence

### T_A

SLOAD diverges at slot 0x8 (address 0x4d96369002fc5b9687ee924d458a7e5baa5df34e, pc 3475)
- Normal: 5fb88aee00000000007dfb20e730e32a06970000000003eb50c012f6bb037676
- Reverse: 5fb88b1900000000007d962f94a1dfb0d0e20000000003ee799c57100378004e

This is written by T_B in the reverse scenario (pc 9554), therefore we overwrite it.

## Partial overwrites

We overwrite the state of T_B with Delta_T_A for the reverse scenario. Thus, all the state changes by T_A are reverted to the prestate of T_A.

For the intermediary transaction 0x8a0f1557a06bf3367681dff765bf9906da98129927ff17a82d0c5cbdd1230034, reverting the changes of T_A also reverts following changes of the intermediary transaction:
- storage@0x4d96369002fc5b9687ee924d458a7e5baa5df34e@0x8
- storage@0x8888801af4d980682e47f1a9036e589479e835c5@0xbba30aa71f0946f41bdea4d6bf4e956e5c5dd7778c8ed70f1721a093bb7be698
- storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0x64e8de5880dcd860292f919bddc0fdf9ede41c0e0a2fdefd99b32c9b41381896

However, it does not revert the following changes which are also accessed by T_B:
- storage@0x8888801af4d980682e47f1a9036e589479e835c5@0x7718372ae9b89f6e2a891d72f64f8d7bfe32f5b677ae8b4a6a3b2594fc712182
- storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0x9c6c36ad38b084cbef50f8da801749f3e2fb41bbc473394ee0dd2d543a7d851a

As such, the changes by this intermediary transaction are partially kept.

## Other notes

Attacker EOA loss instead of gain in our scenario. At least for the replay of T_B we have partial inclusion of an intermediary transaction.