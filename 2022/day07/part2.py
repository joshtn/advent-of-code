import argparse
from functools import lru_cache
import os.path

import pytest

####
from collections import defaultdict



INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# keep track of dirname
# scan each line for number part  then add the number part to a total var.
# until u reach a line that has dir or shifted to left..

path = []
dir_sizes = defaultdict(int) #defaultdict can manipulate when nothing is inside
children = defaultdict(list)


def compute(s: str) -> int:
    blocks = ("\n" + s.strip()).split("\n$ ")[1:]

    for block in blocks:
        parse(block)

    ans = 0
    for abspath in dir_sizes:
        if dfs(abspath) <= 100000:
            ans += dfs(abspath)
            

    return ans




def parse(block):
    
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]

    parts = command.split(" ")
    op = parts[0]
    if op == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])

        return

    abspath = "/".join(path)
    assert op == "ls"

    sizes = []
    for line in outputs:
        if not line.startswith("dir"):
            sizes.append(int(line.split(" ")[0]))
        else:
            dir_name = line.split(" ")[1]
            children[abspath].append(f"{abspath}/{dir_name}")

    dir_sizes[abspath] = sum(sizes)


@lru_cache(None)
def dfs(abspath):
    size = dir_sizes[abspath]
    for child in children[abspath]:
        size += dfs(child)
    return size




INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
EXPECTED = 95437


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
