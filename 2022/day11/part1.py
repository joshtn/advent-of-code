import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# monkey stole items. Worry level is the main variable used in calculations
# divide worry level by 3 and round down to nearest int
# focus on 2 most active monkeys, done by counting total times monkey inspect item in 20 rounds.
# return 2 most active monkey multiplied with each other.
# by looking at input i can see that worry level can increase by adding or multiplying

def compute(s: str) -> int:

    monkeys = []
    for group in s.strip().split("\n\n"):
        monkey = []
        lines = group.splitlines()
        #monkey.append(list(eval(lines[1].split(": ")[1]))) eval() bad practice coz hackers can inject.
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)

    counts = [0] * len(monkeys)

    # monkey[0]: items
    # monkey[1]: operation
    # monkey[2]: test factor
    # monkey[3]: true target
    # monkey[4]: false target

    for _ in range(20):
        for index, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item //= 3
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[index] += len(monkey[0])
            monkey[0] = []
    
    counts.sort()


    return counts[-1] * counts[-2]






INPUT_S = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
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
