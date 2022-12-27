import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# 4 char all diff
# how many chars has been iterated before 4 diff chars
# pointer? string manipluate[::dfdfdf]
# loop with 2 vars, increment each time until 4 diff chars keep a count

def compute(s: str) -> None:
    i = 0
    while True:
        ss = s[i:(i+4)]
        if len(set(list(ss))) == 4:
            print(i + 4)
            break

        i += 1

INPUT_S = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''
EXPECTED = 7


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
