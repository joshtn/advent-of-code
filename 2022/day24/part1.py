import argparse
import os.path

import pytest

####
import math
from collections import deque

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    
    blizzards = tuple(set() for _ in range(4))
    
    for r, line in enumerate(s.splitlines()[1:]):
        for c, item in enumerate(line[1:]):
            if item in "<>^v":
                blizzards["<>^v".find(item)].add((r, c))

    queue = deque([(0, -1, 0)])
    target = (r, c - 1)
    seen = set()

    lcm = r * c // math.gcd(r, c)

    while queue:
        time, cr, cc = queue.popleft()

        time += 1

        for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
            nr = cr + dr
            nc = cc + dc

            if (nr, nc) == target:
                print(time)
                exit(0)

            if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (-1, 0):
                continue

            fail = False

            if (nr, nc) != (-1, 0):
                for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                    if ((nr - tr * time) % r, (nc - tc * time) % c) in blizzards[i]:
                        fail = True
                        break

            if not fail:
                key = (nr, nc, time % lcm)

                if key in seen:
                    continue

                seen.add(key)
                queue.append((time, nr, nc))

    return 0


INPUT_S = '''\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
'''
EXPECTED = 18


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
