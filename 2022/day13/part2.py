import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:


    def f(x, y):
        if type(x) == int:
            if type(y) == int:
                return x - y
            else:
                return f([x], y)
        else:
            if type(y) == int:
                return f(x, [y])

        for a, b in zip(x, y):
            v = f(a, b)
            if v:
                return v

        return len(x) - len(y)


    x = list(map(eval, s.split()))

    i2 = 1
    i6 = 2

    for a in x:
        if f(a, [[2]]) < 0:
            i2 += 1
            i6 += 1
        elif f(a, [[6]]) < 0:
            i6 +=1

    return  i2 * i6






INPUT_S = '''\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''
EXPECTED = 13


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
