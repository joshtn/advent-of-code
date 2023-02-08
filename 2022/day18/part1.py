import argparse
import os.path

import pytest

####


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    
    faces = {}

    offsets = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]

    for line in s.splitlines():
        x, y, z = map(int, line.split(","))

        for dx, dy, dz in offsets:
            k = (x + dx, y + dy, z + dz)
            if k not in faces:
                faces[k] = 0 
            faces[k] += 1


    return list(faces.values()).count(1)






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
