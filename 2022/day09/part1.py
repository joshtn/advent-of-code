import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# grid with numbers each rep tree. Count trees visible
# example input -> curr=[1][1] then check [0][1],[2][1],[1][0],[1],[2]
# think: make a 2d array to rep grid. Class tree, then save state visible_left = bool
# 1 make 2d list : find row_col_num append input to 2d list



def compute(s: str) -> int:
    #s_split = s.split("\n")
    #row_col_count = len(str(s_split[0]))
    #print(row_col_count) 

    grid = [list(map(int, line)) for line in s.splitlines()]

    t = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            if (all(grid[r][x] < k for x in range(c)) or
                    all(grid[r][x] < k for x in range(c + 1, len(grid[r]))) or
                    all(grid[x][c] < k for x in range(r)) or
                    all(grid[x][c] < k for x in range(r + 1, len(grid)))):
                t += 1

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
