# TOD attack analysis

Transactions:
- T_A: [0x226f20bd9780288a81a7ca791deddc80227d26cfb4c2aee9095137fdcfb35cc9](https://etherscan.io/tx/0x226f20bd9780288a81a7ca791deddc80227d26cfb4c2aee9095137fdcfb35cc9)
- T_B: [0x9f806cd962149465f375b163bab16e4117a6f0f0bddcc8c70bd3c608c469eac6](https://etherscan.io/tx/0x9f806cd962149465f375b163bab16e4117a6f0f0bddcc8c70bd3c608c469eac6)

## Ground truth

### Attacker
Asset changes for: [0x860bd2dba9Cd475A61E6d1b45e16c365F6D78F66](https://etherscan.io/address/0x860bd2dba9Cd475A61E6d1b45e16c365F6D78F66)
- ETHER (+0x10aa1e21bfab10b)


### Victim
Asset changes for: [0x005FdE5294199d5C3Eb5Eb7a6E51954123b74b1c](https://etherscan.io/address/0x005FdE5294199d5C3Eb5Eb7a6E51954123b74b1c)
- ERC20_TOKEN (-0x91ffaffc0) https://etherscan.io/token/0x607F4C5BB672230e8672085532f7e901544a7375


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: False
- attacker_eoa_loss: False
- attacker_bot_gain: True
- attacker_bot_loss: True
- victim_gain: False
- victim_loss: True

## Manually parsed logs

Containing attacker:

| Normal T_A                                           | Reverse T_A | Is gain?                  |
|------------------------------------------------------|-------------|---------------------------|
| CALL@860(to: 0xc02..., value: 0x49014b87fffee783)    |             | No  (-0x49014b87fffee783) |
| CALL@7c6(to: 0x860..., value: 0x4a0bed6a1bf9988e)    |             | Yes (+0x4a0bed6a1bf9988e) |
| Transfer@c02(0x860..., 0x6d5..., 0x49014b87fffee783) |             | No (-0x49014b87fffee783)  |
| Transfer@607(0x6d5..., 0x860..., 0x28b3e76b9b7)      |             | net 0 with other          |
| Transfer@607(0x860..., 0x7c6..., 0x28b3e76b9b7)      |             | net 0 with other          |

There is also a Deposit@c02(0x860..., 0x49014b87fffee783) event in the normal scenario (gain of 0x49014b87fffee783)


| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim (not investigated)


## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Yes

## First divergence

### T_A

SLOAD diverges at slot 0x8 (address 0x6d57a53a45343187905aad6ad8ed532d105697c1, pc 3475)
- Normal: 5fb8a3c5000000000015ae38ab4fb9e708aa0000000000000000c487275d4bfa
- Reverse: 5fb8a3cf000000000015d5d5a2075d0950aa0000000000000000c323adc7fce1

This is written by T_B in the reverse scenario (pc 9554), therefore we overwrite it.

## Other notes

Because we do not model the Deposit event, we calculate an attacker loss.