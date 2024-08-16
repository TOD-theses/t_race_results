# TOD checker output

Transactions:
- T_A: [0x1640adc0afcf49d6a786fef4aabcd389c3afb01881fecda3b1befb14cba93823](https://etherscan.io/tx/0x1640adc0afcf49d6a786fef4aabcd389c3afb01881fecda3b1befb14cba93823)
- T_B: [0xdd8366e1509707b0dc81f5372948660bba3e33d3e13a47890625e22bc6d27ad7](https://etherscan.io/tx/0xdd8366e1509707b0dc81f5372948660bba3e33d3e13a47890625e22bc6d27ad7)


Attacker: [0x76f78e3a261b2cac1cb003308235f0332abf7786](https://etherscan.io/address/0x76f78e3a261b2cac1cb003308235f0332abf7786)
Victim: [0x63bd5327d12a93c7265785ced9d7693cadbb40d8](https://etherscan.io/address/0x63bd5327d12a93c7265785ced9d7693cadbb40d8)

Attacker gain tokens:
- ERC-20 [eXRD](https://etherscan.io/token/0x6468e79a80c0eab0f9a2b574c8d5bc374af59414)

Victim loss tokens:
- ERC-20 [eXRD](https://etherscan.io/token/0x6468e79a80c0eab0f9a2b574c8d5bc374af59414)

# Manually parsed logs

Containing attacker:

| Normal T_A                                         | Reverse T_A                                        | Is gain?  |
|----------------------------------------------------|----------------------------------------------------|-----------|
| Transfer(0x76f..., 0x684..., 0xbebc200)            | Transfer(0x76f..., 0x684..., 0xbebc200)            | identical |
| Transfer(0x684..., 0x76f..., 0x5a131d498032aa6982) | Transfer(0x684..., 0x76f..., 0x5a04c80ce0ad210976) | Yes       |

| Normal T_B | Reverse T_B                                         | Is gain? |
|------------|-----------------------------------------------------|----------|

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B | Reverse T_B                                         | Is loss? |
|------------|-----------------------------------------------------|----------|
| <reverted> | Transfer(0x684..., 0x63b..., 0x10f0cf064dd59200000) | Yes      |


# Reverted call contexts?

T_B normal

# Normal scenario logs match Etherscan logs?

Yes

# Other notes

If we considered transaction values, the victim would have Ether gain because T_B is reverted in the normal scenario.