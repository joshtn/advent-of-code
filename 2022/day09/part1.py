import argparse
import os.path

import pytest

####



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# is it a 2d grid similar to last days?
# move func, 1 step  at a time

hx, hy = 0, 0
tx, ty = 0, 0


def compute(s: str) -> int:
    lines = s.strip().split("\n")


    def touching(x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


    def move(dx, dy):
        global hx, hy, tx, ty

        hx += dx
        hy += dy

        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y


    dd = {
        "R": [1, 0],
        "U": [0, 1],
        "L": [-1, 0],
        "D": [0, -1]
    }


    tail_visited = set()
    tail_visited.add((tx, ty))


    for line in lines:
        op, amount = line.split(" ")
        amount = int(amount)
        dx, dy = dd[op]

        for _ in range(amount):
            move(dx, dy)
            tail_visited.add((tx, ty))


    print(len(tail_visited))
            
    return len(tail_visited)






INPUT_S = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
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
