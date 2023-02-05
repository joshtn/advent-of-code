import argparse
import os.path

import pytest

####
from collections import deque


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    valves = {}
    tunnels = {}


    for line in s.splitlines():
        line = line.strip()
        valve = line.split()[1]
        flow = int(line.split(";")[0].split("=")[1])
        targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
        valves[valve] = flow
        tunnels[valve] = targets

    dists = {}
    nonempty = []

    for valve in valves:
        if valve != "AA" and not valves[valve]:
            continue

        if valve != "AA":
            nonempty.append(valve)

        dists[valve] = {valve: 0, "AA": 0}
        visited = {valve}

        queue = deque([(0, valve)])

        while queue:
            distance, position = queue.popleft()
            for neighbor in tunnels[position]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if valves[neighbor]:
                    dists[valve][neighbor] = distance + 1
                queue.append((distance + 1, neighbor))

        del dists[valve][valve]
        if valve != "AA":
            del dists[valve]["AA"]

    indices = {}

    for index, elements in enumerate(nonempty):
        indices[elements] = index

    cache = {}

    def dfs(time, valve, bitmask):
        if (time, valve, bitmask) in cache:
            return cache[(time, valve, bitmask)]

        maxval = 0
        for neighbor in dists[valve]:
            bit = 1 << indices[neighbor]
            if bitmask & bit:
                continue
            remtime = time - dists[valve][neighbor] - 1
            if remtime <= 0:
                continue
            maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)

        cache[(time, valve, bitmask)] = maxval

        return maxval

    b = (1 << len(nonempty)) -1

    m = 0

    for i in range((b + 1) // 2):
        m = max(m, dfs(26, "AA", i) + dfs(26, "AA", b ^ i))


    return m






INPUT_S = '''\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''
EXPECTED = 1651


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
