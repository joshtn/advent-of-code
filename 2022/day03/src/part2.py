import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), '../input.txt')


def compute(s: str) -> int:

    sum = 0

    items = iter(s.splitlines())
    while True:
        try:
            s, = set(next(items)) & set(next(items)) & set(next(items))
        except StopIteration:
            break
        else:
            if s.islower():
                sum += 1 + (ord(s) - ord('a'))
            elif s.isupper():
                sum += 27 + (ord(s) - ord('A'))

    return sum


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
EXPECTED = 70


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
