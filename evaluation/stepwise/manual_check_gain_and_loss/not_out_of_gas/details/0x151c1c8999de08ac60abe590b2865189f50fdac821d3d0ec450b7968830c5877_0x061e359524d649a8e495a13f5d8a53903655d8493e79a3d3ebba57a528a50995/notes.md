# TOD attack analysis

Transactions:
- T_A: [0x151c1c8999de08ac60abe590b2865189f50fdac821d3d0ec450b7968830c5877](https://etherscan.io/tx/0x151c1c8999de08ac60abe590b2865189f50fdac821d3d0ec450b7968830c5877)
- T_B: [0x061e359524d649a8e495a13f5d8a53903655d8493e79a3d3ebba57a528a50995](https://etherscan.io/tx/0x061e359524d649a8e495a13f5d8a53903655d8493e79a3d3ebba57a528a50995)

## Ground truth

### Attacker
Asset changes for: [0xB8db34F834E9dF42F2002CeB7B829DaD89d08E14](https://etherscan.io/address/0xB8db34F834E9dF42F2002CeB7B829DaD89d08E14)
- ERC20_TOKEN (+0x42eca02d42) https://etherscan.io/token/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2


### Victim
Asset changes for: [0xDB208b323A9f0F26E29FEDd9D1DA3A4Cff902D6E](https://etherscan.io/address/0xDB208b323A9f0F26E29FEDd9D1DA3A4Cff902D6E)
- ERC20_TOKEN (-0x6e5d2a) https://etherscan.io/token/0xdAC17F958D2ee523a2206206994597C13D831ec7


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: False
- attacker_eoa_loss: False
- attacker_bot_gain: True
- attacker_bot_loss: False
- victim_gain: True
- victim_loss: False

## Manually parsed logs

Containing attacker (not investigated as we have attacker bot gain)

Containing victim (not investigated)

| Normal T_A                                              | Reverse T_A | Is loss? |
|---------------------------------------------------------|-------------|----------|

| Normal T_B                                              | Reverse T_B                                             | Is loss?  |
|---------------------------------------------------------|---------------------------------------------------------|-----------|
| Transfer@ed0(0xdb2..., 0x7d6..., 0x17b7883c06916600000) | Transfer@ed0(0xdb2..., 0x7d6..., 0x17b7883c06916600000) | identical |
| Transfer@dac(0xd4a..., 0xdb2..., 0x7d6..., 0x2467a109)  | Transfer@dac(0xd4a..., 0xdb2..., 0x7d6..., 0x24679d39)  | No        |


## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Yes

## First divergence (T_B)

SLOAD diverges at slot 0x8 (address 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, pc 3475)
Normal: 5fb8a789000000000000000059fe9e1708f40000000029610006d0e15b84e0bd
Reverse: 5fb8a75b000000000000000059fe9946b22b0000000029610224cba8b955ad81

This is written by T_A, therefore we overwrite it. However, the value written by T_A does not match the normal scenario value, hence an intermediary transaction also has written to this storage slot.


## Partial overwrites

We overwrite the state of T_B with Delta_T_A for the reverse scenario. Thus, all the state changes by T_A are reverted to the prestate of T_A.

For the intermediary transaction 0x0ec339464cfa01d16892fd96e7b9a0005d15795d65e7a4bac89cdafde620e7e9, reverting the changes of T_A also reverts following changes of the intermediary transaction:
- storage@0xdac17f958d2ee523a2206206994597c13d831ec7@0x45b1147656da4d940c556082f0e09e91e3d046c1c84468f8ead64d8fdc1c749a
- storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0xaced72359d8708e95d2112ba70e71fa267967a5588d15e7c78c1904e0debe410
- storage@0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852@0x0000000000000000000000000000000000000000000000000000000000000008

However, it does not revert the following changes which are also accessed by T_B:
- storage@0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852@0x000000000000000000000000000000000000000000000000000000000000000a
- storage@0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852@0x0000000000000000000000000000000000000000000000000000000000000009

As such, the changes by this intermediary transaction are partially kept.

## Other notes

Victim gain and partial overwrites.