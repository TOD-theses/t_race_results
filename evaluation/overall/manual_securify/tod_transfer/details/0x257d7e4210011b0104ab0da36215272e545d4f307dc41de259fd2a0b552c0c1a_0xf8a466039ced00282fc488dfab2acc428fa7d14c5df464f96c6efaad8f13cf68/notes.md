# TOD checker output

Transactions:
- T_A: [0x257d7e4210011b0104ab0da36215272e545d4f307dc41de259fd2a0b552c0c1a](https://etherscan.io/tx/0x257d7e4210011b0104ab0da36215272e545d4f307dc41de259fd2a0b552c0c1a)
- T_B: [0xf8a466039ced00282fc488dfab2acc428fa7d14c5df464f96c6efaad8f13cf68](https://etherscan.io/tx/0xf8a466039ced00282fc488dfab2acc428fa7d14c5df464f96c6efaad8f13cf68)


# Manually checked witness


| Normal T_A    | Reverse T_A   |
|---------------|---------------|

| Normal T_B                                   | Reverse T_B                 |
|----------------------------------------------|-----------------------------|
| CALL@7f3...:417(value: 0x11058e54e218c78000) | CALL@7f3...:417(value: 0x0) |


# Reverted call contexts?

No

# Normal Call matches Etherscan?

Yes

# Other notes

Zero value call in reverse.