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

    width = max(map(len, grid))
    grid = [line + " " * (width - len(line)) for line in grid]

    r = 0
    c = 0
    dr = 0
    dc = 1

    while grid[r][c] != ".":
        c += 1   

    for x, y in re.findall(r"(/d+)([RL]?)", sequence):
        x = int(x)
        for _ in range(x):
            nr = r
            nc = c
            while True:
                nr = (nr + dr) % len(grid)
                nc = (nc + dc) % len(grid[0])
                if grid[nr][nc] != " ":
                    break
            if grid[nr][nc] == "#":
                break
            r = nr
            c = nc
        if y == "R":
            dr, dc = dc, -dr
        elif y == "L":
            dr, dc = -dc, dr


    if dr == 0:
        if dc == 1:
            k = 0 
        else:
            k = 2
    else:
        if dr == 1:
            k = 1 
        else:
            k = 3



    return (1000 * (r + 1) + 4 * (c + 1) + k)






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
