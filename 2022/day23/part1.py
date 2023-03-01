import argparse
import os.path

import pytest

####

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    elves = set()

    for r, line in enumerate(s.splitlines()):
        for c, item in enumerate(line):
            if item == "#":
                elves.add(c + r * 1j)

    scanmap = {
        -1j: [-1j - 1, -1j, -1j + 1],
        1j: [1j - 1, 1j, 1j + 1],
        1: [1 - 1j, 1, 1 + 1j],
        -1: [-1 - 1j, -1, -1 + 1j]
    }

    moves = [-1j, 1j, -1, 1]
    N = [-1 - 1j, -1j, -1j + 1, 1, 1 + 1j, 1j, 1j - 1, -1]

    for _ in range(10):
        once = set()
        twice = set()

        for elf in elves:
            if all(elf + x not in elves for x in N):
                continue
            for move in moves:
                if all(elf + x not in elves for x in scanmap[move]):
                    prop = elf + move
                    if prop in twice:
                        pass
                    elif prop in once:
                        twice.add(prop)
                    else:
                        once.add(prop)
                    break

        ec = set(elves)

        for elf in ec:
            if all(elf + x not in ec for x in N):
                continue
            for move in moves:
                if all(elf + x not in ec for x in scanmap[move]):
                    prop = elf + move
                    if prop not in twice:
                        elves.remove(elf)
                        elves.add(prop)
                    break
        
        moves.append(moves.pop(0))

    mx = min(x.real for x in elves)
    Mx = max(x.real for x in elves)
    my = min(x.imag for x in elves)
    My = max(x.imag for x in elves)

    return ((Mx - mx + 1) * (My - my + 1) - len(elves))






INPUT_S = '''\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
'''
EXPECTED = 110


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
