import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# scenic view score, mult each tree seen for each dir and return highest among all trees.

def compute(s: str) -> int:

    grid = [list(map(int, line)) for line in s.splitlines()]

    t = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            L = R = U = D = 0
            for x in range(c - 1, -1, -1):
                L += 1
                if grid[r][x] >= k:
                    break
            for x in range(c + 1, len(grid)):
                R += 1
                if grid[r][x] >= k:
                    break
            for x in range(r - 1, -1, -1):
                U += 1
                if grid[x][c] >= k:
                    break
            for x in range(r + 1, len(grid)):
                D += 1
                if grid[x][c] >= k:
                    break

            t = max(t, L * R * U * D)

            
    return t






INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 21


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
