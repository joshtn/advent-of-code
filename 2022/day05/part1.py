import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# use 3 lists and pop and append?
# lots of insert and delete operations
# unpack letters in brackets
# regex for seperating str from ints
# seperate input first by the blank line
# for crates do unpack using [1::4]

# update
# get moves/instruction data to be "triplets"


def compute(s: str) -> str:
    state = [
        'FHMTVLD',
        'PNTCJGQH',
        'HPMDSR',
        'FVBL',
        'QLGHN',
        'PMRGDBW',
        'QLHCRNMG',
        'WLC',
        'TMZJQLDR',
    ]

    instructions = [
        'move 1 from 2 to 1',
        'move 3 from 1 to 3',
        'move 2 from 2 to 1',
        'move 1 from 1 to 2',
    ]

    ans = ""



    return ans

"""
    [P]                 [Q]     [T]
[F] [N]             [P] [L]     [M]
[H] [T] [H]         [M] [H]     [Z]
[M] [C] [P]     [Q] [R] [C]     [J]
[T] [J] [M] [F] [L] [G] [R]     [Q]
[V] [G] [D] [V] [G] [D] [N] [W] [L]
[L] [Q] [S] [B] [H] [B] [M] [L] [D]
[D] [H] [R] [L] [N] [W] [G] [C] [R]
 1   2   3   4   5   6   7   8   9 
"""

INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = "CMZ"


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read().strip()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
