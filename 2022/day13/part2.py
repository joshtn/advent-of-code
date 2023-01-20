import argparse
import os.path

import pytest

####
from collections import deque



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# bfs graph, using q
# fewest steps for any elevation "a"

def compute(s: str) -> int:

    grid = [list(x) for x in s.strip().splitlines()]

    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == "S":
                grid[r][c] = "a"
            if item == "E":
                er = r
                ec = c
                grid[r][c] = "z"

    q = deque()
    q.append((0, er, ec))

    vis = {(er, ec)}

    while q:
        d, r, c = q.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr, nc) in vis:
                continue
            if ord(grid[nr][nc]) - ord(grid[r][c]) < -1:
                continue
            if grid[nr][nc] == "a":
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
