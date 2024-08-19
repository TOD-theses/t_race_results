# TOD checker output

Transactions:
- T_A: [0xad92234cff1e875a55364e8a6c16e735bf1fcd3f43f1a3a5189b0f31ee4e580e](https://etherscan.io/tx/0xad92234cff1e875a55364e8a6c16e735bf1fcd3f43f1a3a5189b0f31ee4e580e)
- T_B: [0x926719802c8f84471b9cc6000188295dd71c3ff638375df94d08073cbe07b6f5](https://etherscan.io/tx/0x926719802c8f84471b9cc6000188295dd71c3ff638375df94d08073cbe07b6f5)

# Traces differ?

T_B differs

# Reverted call contexts?

T_B normal
T_B reverse

# Write same storage key according to Etherscan?

No

# Other notes

The ground truth reports that the victim obtained tokens for 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48. This address is contained in the traces of T_B, however T_B reverts in both cases according to our analysis. Hence, no token changes occur.
