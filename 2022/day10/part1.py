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

    x = 1

    o = [0] # padding with 0 so index can start at 1

    for line in lines:
        if line == "noop":
            o.append(x)
        else:
            v = int(line.split()[1])
            o.append(x)
            o.append(x)
            x += v

    o.append(x)

    return sum(x * y for x, y in list(enumerate(o))[20::40])






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
