import argparse
import os.path

import pytest

####


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    rocks = [
        [0, 1, 2, 3],
        [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
        [0, 1, 2, 2 + 1j, 2 + 2j],
        [0, 1j, 2j, 3j],
        [0, 1, 1j, 1 + 1j]
    ]

    jets = [1 if x == ">" else -1 for x in s.strip()]
    solid = {x - 1j for x in range(7)}
    height = 0

    seen = {}

    def summarize():
        o = [-20] * 7

        for x in solid:
            r = int(x.real)
            i = int(x.imag)
            o[r] = max(o[r], i)

        top = max(o)
        return tuple(x - top for x in o)

    rc = 0

    ri = 0
    rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}

    T = 1000000000000

    while rc < T:
        for ji, jet in enumerate(jets):
            moved = {x + jet for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x - 1j for x in rock}
            if moved & solid:
                solid |= rock
                rc += 1 
                height = max(x.imag for x in solid) + 1
                if rc >= T:
                    break
                ri = (ri + 1) % 5
                rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}
                key = (ji, ri, summarize())
                if key in seen:
                    lrc, lh = seen[key]
                    rem = T - rc
                    rep = rem // (rc - lrc)
                    offset = rep * (height - lh)
                    rc += rep * (rc - lrc)
                    seen = {}
                seen[key] = (rc, height)
            else:
                rock = moved
                

    return int(height + offset)






INPUT_S = '''\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''
EXPECTED = 3068


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
