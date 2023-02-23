import argparse
import os.path

import pytest

####
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    grid = []
    done = False

    for line in s.splitlines(True):
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

    for x, y in re.findall(r"(\d+)([RL]?)", sequence):
        x = int(x)
        for _ in range(x):
            cdr = dr
            cdc = dc
            nr = r + dr
            nc = c + dc

            if nr < 0 and 50 <= nc < 100 and dr == -1:
                dr, dc = 0, 1 
                nr, nc = nc + 100, 0
            elif nc < 0 and 150 <= nr < 200 and dc == -1:
                dr, dc = 1, 0
                nr, nc = 0, nr - 100
            elif nr < 0 and 100 <= nc < 150 and dr == -1:
                nr, nc = 199, nc - 100
            elif nr >= 200 and 0 <= nc < 50 and dr == 1:
                nr, nc = 0, nc + 100
            elif nc >= 150 and 0 <= nr < 50 and dc == 1:
                dc = -1
                nr, nc = 149 - nr, 99
            elif nc == 100 and 100 <= nr < 150 and dc == 1:
                dc = -1
                nr, nc = 149 - nr, 149
            elif nr == 50 and 100 <= nc < 150 and dr == 1:
                dr, dc = 0, -1
                nr, nc = nc -  50, 99
            elif nc == 100 and 50 <= nr < 100 and dc == 1:
                dr, dc = -1, 0
                nr, nc = 49, nr + 50
            elif nr == 150 and 50 <= nc < 100 and dr == 1:
                dr, dc = 0, -1
                nr, nc = nc + 100, 49
            elif nc == 50 and 150 <= nr < 200 and dc == 1:
                dr, dc = -1, 0
                nr, nc = 149, nr - 100
            elif nr == 99 and 0 <= nc < 50 and dr == -1:
                dr, dc = 0, 1 
                nr, nc = nc + 50, 50
            elif nc == 49 and 50 <= nr < 100 and dc == -1:
                dr, dc = 1, 0
                nr, nc = 100, nr - 50
            elif nc == 49 and 0 <= nr < 50 and dc == -1:
                dc = 1 
                nr, nc = 149 - nr, 0
            elif nc < 0 and 100 <= nr < 150 and dc == -1:
                dc = 1 
                nr, nc = 149 - nr, 50

            if grid[nr][nc] == "#":
                dr = cdr
                dc = cdc
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
