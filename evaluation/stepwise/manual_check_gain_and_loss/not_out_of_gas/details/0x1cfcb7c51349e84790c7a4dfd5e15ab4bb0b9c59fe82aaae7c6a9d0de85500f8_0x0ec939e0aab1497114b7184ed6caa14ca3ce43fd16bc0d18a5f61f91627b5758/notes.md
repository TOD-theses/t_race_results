# TOD attack analysis

Transactions:
- T_A: [0x1cfcb7c51349e84790c7a4dfd5e15ab4bb0b9c59fe82aaae7c6a9d0de85500f8](https://etherscan.io/tx/0x1cfcb7c51349e84790c7a4dfd5e15ab4bb0b9c59fe82aaae7c6a9d0de85500f8)
- T_B: [0x0ec939e0aab1497114b7184ed6caa14ca3ce43fd16bc0d18a5f61f91627b5758](https://etherscan.io/tx/0x0ec939e0aab1497114b7184ed6caa14ca3ce43fd16bc0d18a5f61f91627b5758)

## Ground truth

### Attacker
Asset changes for: [0x80bb0D87DCe1a94329586Ce9C7d39692bBf44af6](https://etherscan.io/address/0x80bb0D87DCe1a94329586Ce9C7d39692bBf44af6)
- ERC20_TOKEN (+0x438129edf56) https://etherscan.io/token/0xfA5047c9c78B8877af97BDcb85Db743fD7313d4a


### Victim
Asset changes for: [0xa9a57343bA326e9C0aa2EA6F254CA40eD9Fd8c74](https://etherscan.io/address/0xa9a57343bA326e9C0aa2EA6F254CA40eD9Fd8c74)
- ERC20_TOKEN (-0x3f4ab5ca0815d) https://etherscan.io/token/0x8888801aF4d980682e47f1A9036e589479e835C5


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: True
- attacker_eoa_loss: False
- attacker_bot_gain: False
- attacker_bot_loss: False
- victim_gain: True
- victim_loss: False

## Manually parsed logs

Containing attacker (ignored as we also find an Attacker EOA gain without loss)

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                           | Reverse T_B                                          | Is loss? |
|------------------------------------------------------|------------------------------------------------------|----------|
| Transfer@dac(0xa9a..., 0xd4a..., 0x491a8e8)          | Transfer@dac(0xa9a..., 0xd4a..., 0x491a8e8)          |          |
| Transfer@888(0x4d9..., 0xa9a..., 0x11d7bc6c937fca90) | Transfer@888(0x4d9..., 0xa9a..., 0x11d78f327996c600) | No       |



## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Yes

# First divergence

## T_B

SLOAD diverges at slot 0x8 (address 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, pc 3475):
- Normal: 5fb8930c000000000000000059f6794543c400000000297e5fa1426fe79e422f
- Reverse: 5fb892f2000000000000000059f6eb0e485b00000000297e2aecf72f5e55f1f8

This is written by T_A, therefore we overwrite it. However, the value written by T_A does not match the normal scenario value, hence an intermediary transaction also has written to this storage slot.

## Other notes

Victim gain, not loss according to our traces.