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
    ans = ""
    N = 9
    drawing_lines = 8

    data, moves = s.split("\n\n")
    drawing = data.split("\n")
    stacks = [[] for _ in range(N)]

    for i in range(drawing_lines):
        line = drawing[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                stacks[s].append(crates[s])

    # reverse all stacks
    stacks = [stack[::-1] for stack in stacks]


    for line in moves.split("\n"):
        tokens = line.split(" ")
        if tokens[-1] == "": # handles last list that is empty and no move in it
            break
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1

        stacks[dst].extend(stacks[src][-n:]) # takes -n last elements, moves them to dst
        stacks[src] = stacks[src][:-n] # remove the -n elements from src


    tops = [stack[-1] for stack in stacks]
    ans = "".join(tops)


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
def test(input_s: str, expected: str) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
