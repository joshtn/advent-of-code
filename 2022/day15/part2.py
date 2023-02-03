import argparse
import os.path

import pytest

####
import re


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    pattern = re.compile(r"-?\d+")

    lines = [list(map(int, pattern.findall(line))) for line in s.splitlines()]

    M = 4000000

    for Y in range(M + 1):

        intervals = []

        for sx, sy, bx, by in lines:

            d = abs(sx - bx) + abs(sy - by)
            o = d - abs(sy - Y)

            if o < 0:
                continue

            lx = sx - o
            hx = sx + o

            intervals.append((lx, hx))


        intervals.sort()

        q = []

        for lo, hi in intervals:
            if not q:
                q.append([lo, hi])
                continue

            qlo, qhi = q[-1]

            if lo > qhi + 1:
                q.append([lo, hi])
                continue

            q[-1][1] = max(qhi, hi)

        x = 0
        for lo, hi in q:
            if x < lo:
                print(x * 4000000 + Y)
                exit(0)
            x = max(x, hi + 1)
            if x > M:
                break


    return 0






INPUT_S = '''\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''
EXPECTED = 26


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
