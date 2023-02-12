import argparse
import os.path

import pytest

####
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def dfs(bp, maxspend, cache, time, bots, amt):
    if time == 0:
        return amt[3]

    key = tuple([time, *bots, *amt])
    if key in cache:
        return cache[key]

    maxval = amt[3] + bots[3] * time

    for btype, recipe in enumerate(bp):
        if btype != 3 and bots[btype] >= maxspend[btype]:
            continue

        wait = 0
        for ramt, rtype in recipe:
            if bots[rtype] == 0:
                break

            wait = max(wait,-(-(ramt - amt[rtype]) // bots[rtype])) #celling hacky way
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_ = bots[:] # cloning array
            amt_ = [x + y * (wait + 1) for x, y in zip(amt, bots)]
            for ramt, rtype in recipe:
                amt_[rtype] -= ramt
            bots_[btype] += 1
            for i in range(3):
                amt_[i] = min(amt_[i], maxspend[i] * remtime)
            maxval = max(maxval, dfs(bp, maxspend, cache, remtime, bots_, amt_))

    cache[key] = maxval
    return maxval

def compute(s: str) -> int:

    total = 0
    
    for i, line in enumerate(s.splitlines()):
        bp = []
        maxspend = [0, 0, 0]
        for section in line.split(": ")[1].split(". "):
            recipe = []
            for x, y in re.findall(r"(\d+) (\w+)", section):
                x = int(x)
                y = ["ore", "clay", "obsidian"].index(y)
                recipe.append((x, y))
                maxspend[y] = max(maxspend[y], x)
            bp.append(recipe)
        v = dfs(bp, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
        total += (i + 1) * v

    return total






INPUT_S = '''\
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
'''
EXPECTED = 33


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
