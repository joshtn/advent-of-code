import argparse
import os.path

import pytest


INPUT_TXT = os.path.join(os.path.dirname(__file__), '../input.txt')


def compute(s: str) -> int:
    count = 0
    for line in s.splitlines():
        ab, cd = line.split(',')
        a_s, b_s = ab.split('-') 
        c_s, d_s = cd.split('-')
        a, b = int(a_s), int(b_s)
        c, d = int(c_s), int(d_s)

        set_ab = set(range(a, b+1))
        set_cd = set(range(c, d+1))
        overlap_set = set_ab.intersection(set_cd)

        if overlap_set:
            count += 1
      

    return count

INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 4


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
