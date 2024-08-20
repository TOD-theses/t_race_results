# TOD attack analysis

Transactions:
- T_A: [0x5d55a3e83cbe744dcb594df725b7075f7f0fad70b861cf782fb0b73173261a72](https://etherscan.io/tx/0x5d55a3e83cbe744dcb594df725b7075f7f0fad70b861cf782fb0b73173261a72)
- T_B: [0xdedb6818733400663d367e41b54262a47c117f6faa3c00ed47b4a216efb42abd](https://etherscan.io/tx/0xdedb6818733400663d367e41b54262a47c117f6faa3c00ed47b4a216efb42abd)

## Ground truth

### Attacker
Asset changes for: [0x9080EF9a1CD45218e8b857D4EdfD8B5F581199c9](https://etherscan.io/address/0x9080EF9a1CD45218e8b857D4EdfD8B5F581199c9)
- ERC20_TOKEN (+0x7d4d8b3f79f3956a8) https://etherscan.io/token/0x1a23a6BfBAdB59fa563008c0fB7cf96dfCF34Ea1


### Victim
Asset changes for: [0x6d22fDe407bB77C1Ea5b0e7fD3B03Cf961a25879](https://etherscan.io/address/0x6d22fDe407bB77C1Ea5b0e7fD3B03Cf961a25879)
- ERC20_TOKEN (-0xa0616499664b64781) https://etherscan.io/token/0x1a23a6BfBAdB59fa563008c0fB7cf96dfCF34Ea1


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: True
- attacker_bot_gain: True
- attacker_bot_loss: True
- victim_gain: False
- victim_loss: True

## Manually parsed logs

Containing attacker:

| Normal T_A                                           | Reverse T_A                                                   | Is gain? |
|------------------------------------------------------|---------------------------------------------------------------|----------|
| Transfer@dac(0x908..., 0xb2b..., 0x37e0ef9940)       | Transfer@dac(0x908..., 0xb2b..., 0x37e0ef9940) but <reverted> | No       |
| Transfer@1a2(0x0..., 0x908..., 0x3dd668881ed08e3e05) | <reverted>                                                    | Yes      |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim: (ignored, as we also reported victim loss without gain)


## Reverted call contexts?

T_A reverse

## Normal scenario logs match Etherscan logs?

Yes

# First divergence

## T_A

SLOAD diverges at slot 0x1ff7807c49e5ae21765cf875ca8bc8fbe10f58fabe27e6061958b046acc97b80 (address 0xdac17f958d2ee523a2206206994597c13d831ec7, pc 9260):
- Normal: 0000000000000000000000000000000000000000000000000000007587e3fba8
- Reverse: 0000000000000000000000000000000000000000000000000000008b7efcfb2c

The is written by T_B (the reverse value matches our reverse scenario SSTORE at pc 9340).

## Other notes

We observe attacker loss because of a `REVERT` in the reverse scenario.