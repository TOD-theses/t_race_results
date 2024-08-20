import argparse
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterable, Sequence, TypedDict


class Step(TypedDict):
    pc: int
    op: str
    gas: int
    gasCost: int
    depth: int
    stack: list[str]
    memory: list[str]

def compare_traces(trace_normal: Sequence[Step], trace_reverse: Sequence[Step]):
    prev_step_normal = None
    prev_step_reverse = None

    for step_normal, step_reverse in zip(trace_normal, trace_reverse):
        for key in set(step_normal) | set(step_reverse):
            if step_normal.get(key) != step_reverse.get(key):
                return {
                    'previous_steps': {
                        'normal': prev_step_normal,
                        'reverse': prev_step_reverse,
                    },
                    'differing_steps': {
                        'normal': step_normal,
                        'reverse': step_reverse,
                    },
                    'key': key
                }
        prev_step_normal = step_normal
        prev_step_reverse = step_reverse

    if len(trace_normal) != len(trace_reverse):
        i = min(len(trace_normal), len(trace_reverse))
        return {
            'previous_steps': {
                'normal': prev_step_normal,
                'reverse': prev_step_reverse,
            },
            'differing_steps': {
                'normal': i < len(trace_normal) and trace_normal[i],
                'reverse': i < len(trace_reverse) and trace_reverse[i],
            }
        }
    else:
        return None

def load_trace(path: Path) -> Sequence[Step]:
    with open(path) as f:
        data = json.load(f)
        return data['structLogs']

def main():
    parser = argparse.ArgumentParser(description='Find the first step where two traces differ')
    parser.add_argument('trace_normal', type=Path)
    parser.add_argument('trace_reverse', type=Path)
    args = parser.parse_args()

    trace_normal = load_trace(args.trace_normal)
    trace_reverse = load_trace(args.trace_reverse)

    result = compare_traces(trace_normal, trace_reverse)

    if not result:
        print('Traces are equal')
        return None

    print('PC:', set([result['differing_steps']['normal']['pc'], result['differing_steps']['reverse']['pc']]))

    if result['differing_steps']['normal']['op'] == 'SLOAD':
        step_normal = result['differing_steps']['normal']
        step_reverse = result['differing_steps']['reverse']
        slot = step_normal['stack'][-1]
        assert slot == step_reverse['stack'][-1], f'Unexpected SLOAD with different slots'

        print(f'SLOAD diverges at slot {slot}')
        print(f'Normal: {step_normal["storage"][slot[2:].rjust(64, "0")]}')
        print(f'Reverse: {step_reverse["storage"][slot[2:].rjust(64, "0")]}')
    else:
        print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()