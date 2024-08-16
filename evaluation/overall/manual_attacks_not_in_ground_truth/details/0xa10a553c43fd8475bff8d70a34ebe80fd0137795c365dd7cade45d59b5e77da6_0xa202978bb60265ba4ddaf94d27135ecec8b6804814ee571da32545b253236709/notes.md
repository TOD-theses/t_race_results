# TOD checker output

Transactions:
- T_A: [0xa10a553c43fd8475bff8d70a34ebe80fd0137795c365dd7cade45d59b5e77da6](https://etherscan.io/tx/0xa10a553c43fd8475bff8d70a34ebe80fd0137795c365dd7cade45d59b5e77da6)
- T_B: [0xa202978bb60265ba4ddaf94d27135ecec8b6804814ee571da32545b253236709](https://etherscan.io/tx/0xa202978bb60265ba4ddaf94d27135ecec8b6804814ee571da32545b253236709)


Attacker: [0x7104f987277f0c04fb423956970e9b25eefed20e](https://etherscan.io/address/0x7104f987277f0c04fb423956970e9b25eefed20e) (bot)
Victim: [0xafdfcb701aa4ca27e44c1e10d33862ba1ae41c4a](https://etherscan.io/address/0xafdfcb701aa4ca27e44c1e10d33862ba1ae41c4a)

Attacker gain tokens:
- ERC-20 [USDN](https://etherscan.io/token/0x674c6ad92fd080e4004b2312b45f796a192d27a0)

Victim loss tokens:
- ERC-20 [WAVES](https://etherscan.io/token/0x1cf4592ebffd730c7dc92c1bdffdfc3b9efcf29a)

# Manually parsed logs

Containing attacker:

| Normal T_A                                                | Reverse T_A | Is gain? |
|-----------------------------------------------------------|-------------|----------|
| Transfer@1cf...(0x710..., 0xdbc..., 0x2)                  |             |          |
| Transfer@67a...(0x710..., 0xdbc..., 0x2)                  |             |          |
| Transfer@1cf...(0xdbc..., 0x710..., 0x2)                  |             |          |
| Transfer@67a...(0xdbc..., 0x710..., 0x1201be5c8b1546002e) |             |          |

| Normal T_B | Reverse T_B                                              | Is gain? |
|------------|----------------------------------------------------------|----------|

Overall:
- attacker gains 0x1201be5c8b1546002c = 332167032918812000300 USDN

Containing victim:

| Normal T_A | Reverse T_A | Is loss? |
|------------|-------------|----------|

| Normal T_B | Reverse T_B                                              | Is loss? |
|------------|----------------------------------------------------------|----------|
| <reverted> | Transfer@1cf...(0xdbc..., 0xafd..., 0x2b23c00a446afc488) | Yes      |


# Reverted call contexts?

T_B normal

# Normal scenario logs match Etherscan logs?

Yes

# Other notes
