# TOD checker output

Transactions:
- T_A: [0x1c22ee81b3ce5d8546e80647edcdd8f472554ca1b692879a7cfb80ef114dc8bd](https://etherscan.io/tx/0x1c22ee81b3ce5d8546e80647edcdd8f472554ca1b692879a7cfb80ef114dc8bd)
- T_B: [0xccfa072446c7771af43429ef0f541d7c2f02694313b9899a62dac78a7e1d8be1](https://etherscan.io/tx/0xccfa072446c7771af43429ef0f541d7c2f02694313b9899a62dac78a7e1d8be1)


Attacker: [0x5fce529a66e43fca22cf28f2fe0640be0bbbced4](https://etherscan.io/address/0x5fce529a66e43fca22cf28f2fe0640be0bbbced4) (bot)
Victim: [0xc5d496bccf6780d2fc61ec31df37a887387bb114](https://etherscan.io/address/0xc5d496bccf6780d2fc61ec31df37a887387bb114)

Attacker gain tokens:
- ERC-20 [FAC](https://etherscan.io/token/0x6d4e4388c0d71740f99670bb58d37eb1480b4458)

Victim loss tokens:
- ERC-20 [FAC](https://etherscan.io/token/0x6d4e4388c0d71740f99670bb58d37eb1480b4458)

# Manually parsed logs

Containing attacker:

| Normal T_A                                      | Reverse T_A                                     | Is gain?                     |
|-------------------------------------------------|-------------------------------------------------|------------------------------|
| Transfer(0x0, 0x5fc..., 0x6ee0bf1912c715a7627)  |                                                 | Yes (+0x6ee0bf1912c715a7627) |
| Transfer(0x76e..., 0x5fc..., 0x15a4c419a9475ce) | Transfer(0x76e..., 0x5fc..., 0x15a4c419a9475ce) | identical                    |

| Normal T_B                                          | Reverse T_B                                         | Is gain?                    |
|-----------------------------------------------------|-----------------------------------------------------|-----------------------------|
| Transfer(0x0, 0x5fc..., 0x1e96465f31516713b1)       | Transfer(0x0, 0x5fc..., 0x70ca237f05dc2c189d9)      | No (-0x6ee0bf1912c715a7628) |
| Transfer(0x5fc..., 0xc5d..., 0x1a24d246f60e45d01bc) | Transfer(0x5fc..., 0xc5d..., 0x1a2f6a9088b4e41c765) | Yes (+0xa984992a69e4c5a9)   |

Overall:
- Gain of 0xa984992a69e4c5a8 = 12215056496779904424

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B                                          | Reverse T_B                                         | Is loss? |
|-----------------------------------------------------|-----------------------------------------------------|----------|
| Transfer(0x5fc..., 0xc5d..., 0x1a24d246f60e45d01bc) | Transfer(0x5fc..., 0xc5d..., 0x1a2f6a9088b4e41c765) | Yes      |


# Reverted call contexts?

No

# Normal scenario logs match Etherscan logs?

Yes

# Other notes
