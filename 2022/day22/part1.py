import argparse
import os.path

import pytest

####
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    grid = []
    done = False

    for line in s.splitlines():
        line = line[:-1]
        if line == "":
            done = True
        if done:
            sequence = line
        else:
            grid.append(line)

    r = 0
    c = 0

    while grid[r][c] != ".":
        c += 1   

    for x, y in re.findall(r"(/d+)([RL]?)", sequence):
        x = int(x)


    return 0






INPUT_S = '''\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
'''
EXPECTED = 6032


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
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
