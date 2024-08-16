# TOD checker output

Transactions:
- T_A: [0xe14585e2c3629a19a76b2799b5d4fbcbabbb86eeb7b7c0cd1114f35f6db2bcec](https://etherscan.io/tx/0xe14585e2c3629a19a76b2799b5d4fbcbabbb86eeb7b7c0cd1114f35f6db2bcec)
- T_B: [0x3207b3c9c69b66d9edc176dc25016eb8a1983fe73e072102855333eaa5f8be43](https://etherscan.io/tx/0x3207b3c9c69b66d9edc176dc25016eb8a1983fe73e072102855333eaa5f8be43)


Attacker: [0x8f6485f44c56e9a8f496e1589d27bc8256233e0d](https://etherscan.io/address/0x8f6485f44c56e9a8f496e1589d27bc8256233e0d)
Victim: [0x525208dd0b56c27bd10703bd675fca0509a17154](https://etherscan.io/address/0x525208dd0b56c27bd10703bd675fca0509a17154)

Attacker gain tokens:
- ERC-20 [ICHI](https://etherscan.io/token/0x903bef1736cddf2a537176cf3c64579c3867a881)

Victim loss tokens:
- ERC-20 [ICHI](https://etherscan.io/token/0x903bef1736cddf2a537176cf3c64579c3867a881)

# Manually parsed logs

Containing attacker:

| Normal T_A                                  | Reverse T_A | Is gain? |
|---------------------------------------------|-------------|----------|
| Transfer(0x4ea..., 0x8f6..., 0x13a03637610) | <reverted>  | Yes      |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B | Reverse T_B                                | Is loss? |
|------------|--------------------------------------------|----------|
| <reverted> | Transfer(0x4ea..., 0x525..., 0x524085c913) | Yes      |


# Reverted call contexts?

T_A reverse
T_B normal

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

If we considered transaction value, then we would have attacker loss because of the transaction revert.