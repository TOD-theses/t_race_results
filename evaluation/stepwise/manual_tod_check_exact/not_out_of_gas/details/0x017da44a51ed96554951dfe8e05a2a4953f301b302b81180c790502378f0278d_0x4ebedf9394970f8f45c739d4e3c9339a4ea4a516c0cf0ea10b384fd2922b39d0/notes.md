# TOD checker output

Transactions:
- T_A: [0x017da44a51ed96554951dfe8e05a2a4953f301b302b81180c790502378f0278d](https://etherscan.io/tx/0x017da44a51ed96554951dfe8e05a2a4953f301b302b81180c790502378f0278d)
- T_B: [0x4ebedf9394970f8f45c739d4e3c9339a4ea4a516c0cf0ea10b384fd2922b39d0](https://etherscan.io/tx/0x4ebedf9394970f8f45c739d4e3c9339a4ea4a516c0cf0ea10b384fd2922b39d0)

# Traces differ?

T_A differs
T_B differs

# Reverted call contexts?

No

# Write same storage key according to Etherscan?

Yes, at several contracts and storage slots.

# Other notes

TOD when using Reth and removing the `_remove_gas_cost_changes` calls in the TOD checker.

Using Erigon, individual transactions differ, but overall no TOD:

```
Tx B: 3
<changes differ: balance@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2 normal: +0x2310f21723f9795 | reverse: +0x230aa35d6c45c1d>
<changes differ: storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0x27cf5658f84e21e719335f0ea86c51c39f098030f918e824fcdea8563ce82957 normal: +0x2310f21723f9795 | reverse: +0x230aa35d6c45c1d>
<changes differ: storage@0xcff0ac508c5c7d24f237de246141821a689ceaf2@0x0000000000000000000000000000000000000000000000000000000000000008 normal: +0x2310f21723f9794fffffffffffff21f494c589c0000 | reverse: +0x230aa35d6c45c1cfffffffffffff21f494c589c0000>

Tx A: 3
<changes differ: balance@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2 normal: +0x230aa35d6c45c1d | reverse: +0x2310f21723f9795>
<changes differ: storage@0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2@0x27cf5658f84e21e719335f0ea86c51c39f098030f918e824fcdea8563ce82957 normal: +0x230aa35d6c45c1d | reverse: +0x2310f21723f9795>
<changes differ: storage@0xcff0ac508c5c7d24f237de246141821a689ceaf2@0x0000000000000000000000000000000000000000000000000000000000000008 normal: +0x230aa35d6c45c1cfffffffffffff21f494c589c0000 | reverse: +0x2310f21723f9794fffffffffffff21f494c589c0000>
```