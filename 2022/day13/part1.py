import argparse
import os.path

import pytest

####
from collections import deque



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    x = list(map(str.splitlines, s.strip().split("\n\n")))

    def f(x, y):
        if type(x) == int:
            if type(y) == int:
                return x - y
            else:
                return f([x], y)
        else:
            if type(y) == int:
                return f(x, [y])

        for a, b in zip(x, y):
            v = f(a, b)
            if v:
                return v

        return len(x) - len(y)

    t = 0

    for i, (a, b) in enumerate(x):
        if f(eval(a), eval(b)) < 0:
            t += i + 1

    return t






INPUT_S = '''\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''
EXPECTED = 13


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
