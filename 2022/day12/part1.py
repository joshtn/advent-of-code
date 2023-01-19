import argparse
import os.path

import pytest

####
from collections import deque



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# a - z with a lowest. 
# S is Currpos. 
# E is best signal. Get to E in few steps. 
# bfs graph, using q

def compute(s: str) -> int:

    grid = [list(x) for x in s.strip().splitlines()]

    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == "S":
                sr = r
                sc = c
                grid[r][c] = "a"
            if item == "E":
                er = r
                ec = c
                grid[r][c] = "z"

    q = deque()
    q.append((0, sr, sc))

    vis = {(sr, sc)}

    while q:
        d, r, c = q.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr, nc) in vis:
                continue
            if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
                continue
            if nr == er and nc == ec:
                return d + 1

            vis.add((nr, nc))
            q.append((d + 1, nr, nc))


    return 0






INPUT_S = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''
EXPECTED = 31


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
