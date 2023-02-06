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

    rc = 0

    ri = 0
    rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}

    while rc < 2022:
        for jet in jets:
            moved = {x + jet for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x - 1j for x in rock}
            if moved & solid:
                solid |= rock
                rc += 1 
                height = max(x.imag for x in solid) + 1
                if rc >= 2022:
                    break
                ri = (ri + 1) % 5
                rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}
            else:
                rock = moved
                

    return int(height)






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
