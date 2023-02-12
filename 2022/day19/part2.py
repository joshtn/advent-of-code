import argparse
import os.path

import pytest

####
from collections import deque


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    
    faces = {}

    offsets = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]

    mx = my = mz = float("inf")
    Mx = My = Mz = -float("inf")

    droplet = set()


    for line in s.splitlines():
        x, y, z = cell = tuple(map(int, line.split(",")))
        droplet.add(cell)

        mx = min(mx, x)
        my = min(my, y)
        mz = min(mz, z)

        Mx = max(Mx, x)
        My = max(My, y)
        Mz = max(Mz, z)



        for dx, dy, dz in offsets:
            k = (x + dx, y + dy, z + dz)
            if k not in faces:
                faces[k] = 0 
            faces[k] += 1

    mx -= 1
    my -= 1
    mz -= 1

    Mx += 1
    My += 1
    Mz += 1

    q = deque([(mx, my, mz)])
    air = {(mx, my, mz)}

    while q:
        x, y ,z = q.popleft()

        for dx, dy, dz in offsets:
            nx, ny, nz = k = (x + dx * 2, y + dy * 2, z + dz * 2)

            if not (mx <= nx <= Mx and my <= ny <= My and mz <= nz <= Mz):
                continue

            if k in droplet or k in air:
                continue

            air.add(k)
            q.append(k)

    free = set()

    for x, y, z in air:
        for dx, dy, dz in offsets:
            free.add((x + dx, y + dy, z + dz))


    return len(set(faces) & free)






INPUT_S = '''\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''
EXPECTED = 64


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
