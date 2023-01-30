import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    blocked = set()
    abyss = 0

    
    lines = s.strip().split("\n")

    # for line in lines:
    #     coords = []

    #     for str_coord in line.split(" -> "):
    #         x, y = map(int, str_coord.split(","))
    #         coords.append((x, y))

    #     print(coords)
    for line in lines:
        x = [list(map(int, p.split(","))) for p in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    blocked.add(x + y * 1j)
                    abyss = max(abyss, y + 1)

    t = 0

    while 500 not in blocked:
        s = 500
        while True:
            if s.imag >= abyss:
                break
            if s + 1j not in blocked:
                s += 1j
                continue
            if s + 1j - 1 not in blocked:
                s += 1j - 1
                continue
            if s + 1j + 1 not in blocked:
                s += 1j + 1
                continue
            break
        blocked.add(s)
        t += 1

    print(t)

    return 0






INPUT_S = '''\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''
EXPECTED = 24


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
