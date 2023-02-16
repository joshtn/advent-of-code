import argparse
import os.path

import pytest

####
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    class Node:
        def __init__(self, n):
            self.n = n
            self.left = None
            self.right = None


    x = [Node(int(x)) for x in s.splitlines()]

    for i in range(len(x)):
        x[i].right = x[(i + 1) % len(x)]
        x[i].left = x[(i - 1) % len(x)]

    m = len(x) - 1

    for c in x:
        if c.n == 0:
            z = c
            continue
        p = c
        if c.n > 0:
            for _ in range(c.n % m):
                p = p.right
            if c == p:
                continue
            c.right.left = c.left
            c.left.right = c.right
            p.right.left = c
            c.right = p.right
            p.right = c
            c.left = p


        else:
            for _ in range(-c.n % m):
                p = p.left
            if c == p:
                continue
            c.left.right = c.right
            c.right.left = c.left
            p.left.right = c
            c.left = p.left
            p.left = c
            c.right = p

    t = 0

    for _ in range(3):
        for _ in range(1000):
            z = z.right
        t += z.n

    return t






INPUT_S = '''\
1
2
-3
3
-2
0
4
'''
EXPECTED = 3


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
