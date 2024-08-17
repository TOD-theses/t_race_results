# TOD checker output

Transactions:
- T_A: [0x13b3e077dc6b620d73bfe06ecebeecc79497256fb55f07cdae1495b5f1d80955](https://etherscan.io/tx/0x13b3e077dc6b620d73bfe06ecebeecc79497256fb55f07cdae1495b5f1d80955)
- T_B: [0x2a05234ff36419e3c866c789768ad051ef2e0e53590a79daee4ce26ea16ecc68](https://etherscan.io/tx/0x2a05234ff36419e3c866c789768ad051ef2e0e53590a79daee4ce26ea16ecc68)


# Manually checked witness


| Normal T_A    | Reverse T_A   |
|---------------|---------------|

| Normal T_B | Reverse T_B                                 |
|------------|---------------------------------------------|
|            | CALL@7a2...:9129(value: 0x12653f2be45e99ba) |


# Reverted call contexts?

T_A reverse

# Normal Call matches Etherscan?

Yes

# Other notes

T_B has reverted internal calls in the normal scenario.
