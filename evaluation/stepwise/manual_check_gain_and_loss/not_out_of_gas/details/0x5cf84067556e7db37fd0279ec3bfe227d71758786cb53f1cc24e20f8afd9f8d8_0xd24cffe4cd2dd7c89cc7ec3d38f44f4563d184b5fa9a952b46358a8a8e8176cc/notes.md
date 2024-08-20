# TOD attack analysis

Transactions:
- T_A: [0x5cf84067556e7db37fd0279ec3bfe227d71758786cb53f1cc24e20f8afd9f8d8](https://etherscan.io/tx/0x5cf84067556e7db37fd0279ec3bfe227d71758786cb53f1cc24e20f8afd9f8d8)
- T_B: [0xd24cffe4cd2dd7c89cc7ec3d38f44f4563d184b5fa9a952b46358a8a8e8176cc](https://etherscan.io/tx/0xd24cffe4cd2dd7c89cc7ec3d38f44f4563d184b5fa9a952b46358a8a8e8176cc)

## Ground truth

### Attacker
Asset changes for: [0x860bd2dba9Cd475A61E6d1b45e16c365F6D78F66](https://etherscan.io/address/0x860bd2dba9Cd475A61E6d1b45e16c365F6D78F66)
- ETHER (+0x17635aea6b46f03)


### Victim
Asset changes for: [0x2570968a0d7243fAF14f8F5C9Eb958dc3d197C4e](https://etherscan.io/address/0x2570968a0d7243fAF14f8F5C9Eb958dc3d197C4e)
- ETHER (-0x1b17f938240811)


## Tool properties output

- attacker_gain_and_victim_loss: False
- attacker_eoa_gain: False
- attacker_eoa_loss: False
- attacker_bot_gain: False
- attacker_bot_loss: False
- victim_gain: False
- victim_loss: False

## Manually parsed logs

Not parsed, as our traces are identical in the normal and reverse scenario.


## Reverted call contexts?

No

## Normal scenario logs match Etherscan logs?

Not checked.

## Other notes

Only collisions between T_A and T_B according to RPC prestates (see json files) and Etherscan state changes:
- balance of WETH (https://etherscan.io/address/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)

According to our normal scenario traces, T_A has three executions of `SELFBALANCE` and T_B has two executions of `SELFBALANCE`, however none of these are by WETH. None of them calls `BALANCE`. Etherscan reports the same number of steps (15171 and 9164), thus we assume we execute the same instructions as on the blockchain.

Etherscan also reports no calls to fail, thus the access of the balance through calls (`CALL`, `CALLCODE`, `CREATE`, `CREATE2`, `SELFDESTRUCT`) should also cause no TOD.

Therefore, no TOD can occur.



