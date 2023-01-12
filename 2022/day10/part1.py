import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# count to act as timer, condition for the important  20th 60th + 40 each time 
# input is simple to work with.
# consider that instructions that different cycles to complete.
# save values into stack and pop at right cycle count, no need



def compute(s: str) -> int:
    lines = s.strip().split("\n")

    X = 1
    op = 0

    ans = 0
    interesting = [20, 60, 100, 140, 180, 220]

    for line in lines:
        parts = line.split(" ")

        if parts[0] == "noop":
            op += 1

            if op in interesting:
                ans += op * X

        elif parts[0] == "addx":
            V = int(parts[1])
            X += V

            op += 1

            if op in interesting:
                ans += op * (X - V)

            op += 1

            if op in interesting:
                ans += op * (X - V)

    return ans






INPUT_S = '''\
noop
addx 3
addx -5
'''
EXPECTED = -1


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
