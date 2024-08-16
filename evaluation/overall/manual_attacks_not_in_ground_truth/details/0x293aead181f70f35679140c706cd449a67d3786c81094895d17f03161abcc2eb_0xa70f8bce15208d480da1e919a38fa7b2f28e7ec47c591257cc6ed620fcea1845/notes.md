# TOD checker output

Transactions:
- T_A: [0x293aead181f70f35679140c706cd449a67d3786c81094895d17f03161abcc2eb](https://etherscan.io/tx/0x293aead181f70f35679140c706cd449a67d3786c81094895d17f03161abcc2eb)
- T_B: [0xa70f8bce15208d480da1e919a38fa7b2f28e7ec47c591257cc6ed620fcea1845](https://etherscan.io/tx/0xa70f8bce15208d480da1e919a38fa7b2f28e7ec47c591257cc6ed620fcea1845)


Attacker: [0x3893e64d7d4cfccf0420acb4cd087f7ba68dc19f](https://etherscan.io/address/0x3893e64d7d4cfccf0420acb4cd087f7ba68dc19f)
Victim: [0x85637cfbbdfeff3bcbd017c5c8bc7897bc2b9f38](https://etherscan.io/address/0x85637cfbbdfeff3bcbd017c5c8bc7897bc2b9f38)

Attacker gain tokens:
- ERC-20 [SFR](https://etherscan.io/token/0x8ab98c28295ea3bd2db6ac8b3ca57a625c054bd1)

Victim loss tokens:
- ERC-20 [SFR](https://etherscan.io/token/0x8ab98c28295ea3bd2db6ac8b3ca57a625c054bd1)

# Manually parsed logs

Containing attacker:

| Normal T_A                                       | Reverse T_A | Is gain? |
|--------------------------------------------------|-------------|----------|
| Transfer(0x28f..., 0x389..., 0x1ff27aa887bf19ff) | <reverted>  | Yes      |

| Normal T_B | Reverse T_B | Is gain? |
|------------|-------------|----------|

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B | Reverse T_B                                      | Is loss? |
|------------|--------------------------------------------------|----------|
| <reverted> | Transfer(0x28f..., 0x856..., 0x317aadc7e56329f7) | Yes      |


# Reverted call contexts?

T_A reverse
T_B normal

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

This would not count as an attack if we consider transaction values (our assumption in the definition was, that this is always equal. This is not the case when transactions are reverted.)