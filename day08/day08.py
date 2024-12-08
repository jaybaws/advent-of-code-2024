from typing import Dict, List, Tuple, Set
from itertools import product


with open("day08/input.txt", "r") as f:
    map = [ [ *line.strip() ] for line in f.readlines() ]
    H:int = len(map)
    W:int = len(map[0])
    antennas:Dict[str, List[Tuple[int, int]]] = {}
    for r, row in enumerate(map):
        for c, f in enumerate(row):
            if f != '.':
                if f not in antennas:
                    antennas[f] = list()
                antennas[f].append((r, c))


def part1() -> int:
    antinodes:Set[Tuple[int, int]] = set()
    for f in antennas:
        for (ar, ac),(br, bc) in product(antennas[f], antennas[f]):
            if (ar, ac) != (br, bc):
                dr, dc = br - ar, bc - ac
                nr, nc = br + dr, bc + dc

                if (0 <= nc < W) and (0 <= nr < H):
                    antinodes.add((nr, nc))

    return len(antinodes)


def part2() -> int:
    antinodes:Set[Tuple[int, int]] = set()
    for f in antennas:
        for (ar, ac),(br, bc) in product(antennas[f], antennas[f]):
            if (ar, ac) != (br, bc):
                dr, dc = br - ar, bc - ac
                nr, nc = br, bc
                while (0 <= nc < W) and (0 <= nr < H):
                    antinodes.add((nr, nc))
                    nr, nc = nr + dr, nc + dc

    return len(antinodes)


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")