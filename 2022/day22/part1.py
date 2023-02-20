import argparse
import os.path

import pytest

####

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    monkeys = {}

    x = [line for line in s.splitlines()]

    for a in x:
        name, expr = a.split(": ")
        if expr.isdigit():
            monkeys[name] = int(expr)
        else:
            left, op, right = expr.split()
            if left in monkeys and right in monkeys:
                monkeys[name] = eval(f"{monkeys[left]} {op} {monkeys[right]}")
            else:
                x.append(a)
    return monkeys["root"]






INPUT_S = '''\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
'''
EXPECTED = 152


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
