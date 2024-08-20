import argparse
import csv
import json
from pathlib import Path
from typing import Any, Counter, Iterable

import requests

provider = 'http://localhost:8124/eth'

def compare_state_diffs(tx_a: str, tx_b: str):
    state_diffs = get_state_diffs_between_transactions(tx_a, tx_b)
    prestates = get_prestates_between_transactions(tx_a, tx_b)
    candidate_written_state_keys = set()
    tx_a_written_state_keys = set(iterate_storage_keys(state_diffs[0]['result']))
    tx_b_written_state_keys = set(iterate_storage_keys(state_diffs[-1]['result']))
    tx_a_accessed_state_keys = set(iterate_storage_keys(prestates[0]['result']))
    tx_b_accessed_state_keys = set(iterate_storage_keys(prestates[-1]['result']))
    intermediary_transactions_with_collisions = set()
    intermediary_collisions_tx_a = set()
    intermediary_collisions_tx_b = set()
    missing_collisions = set()
    overlapping_collisions = set()

    for state_key in storage_collisions(state_diffs[0]['result']['post'], state_diffs[-1]['result']['pre']):
        if state_key[0] == 'storage':
            candidate_written_state_keys.add(state_key)

    for state_diff in state_diffs[1:-1]:
        tx_x_poststate = state_diff['result']['post']
        for state_key in candidate_written_state_keys:
            if has_state_key(tx_x_poststate, state_key):
                intermediary_transactions_with_collisions.add(state_diff['txHash'])
        
    for tx_x in intermediary_transactions_with_collisions:
        state_changes = next(s for s in state_diffs if s['txHash'] == tx_x)
        tx_x_poststate = state_changes['result']['post']
        for state_key in iterate_storage_keys(tx_x_poststate):
            if state_key in candidate_written_state_keys:
                overlapping_collisions.add(state_key)
            else:
                missing_collisions.add(state_key)

    tx_b_reverse_relevant_overwrites = set(storage_collisions(state_diffs[0]['result']['post'], prestates[-1]['result']))
    result = {
        'tx_b_overwritten_write_accesses': [],
        'tx_b_kept_write_accesses': [],
    }

    for state_diff in state_diffs[1:-1]:
        tx_x_poststate = state_diff['result']['post']
        state_writing_keys = set(iterate_storage_keys(tx_x_poststate))

        # writes, where Delta_X_n - Delta_T_A undoes the change of Delta_T_X (by overwriting it with the prestate of T_A)
        overwritten_writes = state_writing_keys & tx_b_reverse_relevant_overwrites
        # writes, that Delta_X_n - Delta_T_A does not modify
        kept_writes = state_writing_keys - tx_b_reverse_relevant_overwrites

        # it is bad if we have writes that are undone and writes that are kept
        # and both are accessed by T_B
        tx_b_overwritten_writes_accesses = overwritten_writes & tx_b_accessed_state_keys
        tx_b_kept_writes_accesses = kept_writes & tx_b_accessed_state_keys
        if tx_b_overwritten_writes_accesses and tx_b_kept_writes_accesses:
            for state_key in tx_b_overwritten_writes_accesses:
                result['tx_b_overwritten_write_accesses'].append({
                    'state_key': state_key,
                    'tx_a_poststate': get_storage_slot_value(state_diffs[0]['result']['post'], state_key),
                    'tx_b_prestate': get_storage_slot_value(prestates[-1]['result'], state_key),
                    'tx_x_poststate': get_storage_slot_value(tx_x_poststate, state_key),
                    'tx_x': state_diff['txHash'],
                })
            for state_key in tx_b_kept_writes_accesses:
                result['tx_b_kept_write_accesses'].append({
                    'state_key': state_key,
                    'tx_b_prestate': get_storage_slot_value(prestates[-1]['result'], state_key),
                    'tx_x_poststate': get_storage_slot_value(tx_x_poststate, state_key),
                    'tx_x': state_diff['txHash'],
                })

    return result


def get_state_diffs_between_transactions(tx_a: str, tx_b: str):
    blocks = range(get_block_for_transaction(tx_a), get_block_for_transaction(tx_b) + 1)
    state_diffs = []
    for n in blocks:
        state_diffs.extend(get_block_state_diff(n))
    
    start = next(i for i, v in enumerate(state_diffs) if v['txHash'] == tx_a)
    end = next(i for i, v in enumerate(state_diffs) if v['txHash'] == tx_b)
    return state_diffs[start:end+1]

def get_prestates_between_transactions(tx_a: str, tx_b: str):
    blocks = range(get_block_for_transaction(tx_a), get_block_for_transaction(tx_b) + 1)
    state_diffs = []
    for n in blocks:
        state_diffs.extend(get_block_prestates(n))

    start = next(i for i, v in enumerate(state_diffs) if v['txHash'] == tx_a)
    end = next(i for i, v in enumerate(state_diffs) if v['txHash'] == tx_b)
    return state_diffs[start:end+1]

def get_block_state_diff(block_number: int):
    return rpc('debug_traceBlockByNumber', [
        hex(block_number),
        {"tracer": "prestateTracer", "tracerConfig": { "diffMode": True } },
    ])

def get_block_prestates(block_number: int):
    return rpc('debug_traceBlockByNumber', [
        hex(block_number),
        {"tracer": "prestateTracer", "tracerConfig": { "diffMode": False } },
    ])


def get_block_for_transaction(tx_hash: str) -> int:
    tx = rpc('eth_getTransactionByHash', [tx_hash])
    return int(tx['blockNumber'], 16)

def rpc(method: str, params: list) -> Any:
    res = requests.post(provider, json={
        'id': 1,
        'method':method,
        'params': params,
        'jsonrpc': '2.0',
    })
    res.raise_for_status()
    data = res.json()
    if 'error' in data:
        raise Exception(f'RPC request failed: {data["error"]}')

    return data['result']

def storage_collisions(state_a: dict, state_b: dict) -> list[tuple[str, str, str]]:
    colls = []

    for addr in set(state_a) & set(state_b):
        for type in set(state_a[addr]) & set(state_b[addr]):
            if type != 'storage':
                continue
            for slot in set(state_a[addr][type]) & set(state_b[addr][type]):
                colls.append((type, addr, slot))

    return colls

def has_state_key(state: dict, state_key: tuple[str, str, str | None]) -> bool:
    type, addr, slot = state_key
    if addr not in state:
        return False
    if type not in state[addr]:
        return False
    if slot and slot not in state[addr][type]:
        return False
    return True

def get_storage_slot_value(state: dict, state_key: tuple[str, str, str]) -> str:
    assert has_state_key(state, state_key), f'Could not find state key: {state_key}'
    type, addr, slot = state_key
    return state[addr][type][slot]

def iterate_storage_keys(state: dict) -> Iterable[tuple[str, str, str]]:
    for addr, account in state.items():
        for slot in account.get('storage', {}):
            yield ('storage', addr, slot)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('samples_csv', type=Path)
    args = parser.parse_args()

    with open(args.samples_csv, newline='') as f:
        reader = csv.DictReader(f)
        # print('tx_a,tx_b,colliding_intermediary_transactions,overlapping_collisions,missing_collisions')
        for row in reader:
            tx_a, tx_b = row['tx_a'], row['tx_b']
            result = compare_state_diffs(tx_a, tx_b)

            with open(Path(f'{tx_a}_{tx_b}') / 'partial_overwrites.json', 'w') as results_file:
                json.dump(result, results_file, indent=2)

if __name__ == '__main__':
    main()