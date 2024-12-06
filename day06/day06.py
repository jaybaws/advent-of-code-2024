from typing import List, Set, Tuple

NORTH, SOUTH, EAST, WEST = (-1, 0), (1, 0), (0, 1), (0, -1)
MOVEMENT_PATTERN = { NORTH:EAST, EAST:SOUTH, SOUTH:WEST, WEST:NORTH }

with open("day06/input.txt", "r") as f:
    LAB = [ [ *s.strip() ] for s in f.readlines() ]
    H = len(LAB)
    W = len(LAB[0])
    for r in range(H):
        for c in range(W):
            if LAB[r][c] == '^':
                start_r = r
                start_c = c


def part1() -> Tuple[int, List[Tuple]]:
    seen_coords:Set[Tuple] = set()
    r, c, (dr, dc) = start_r, start_c, NORTH
    while True:
        seen_coords.add((r, c))

        if not(0<=r+dr<H and 0<=c+dc<W):
            break
      
        if LAB[r+dr][c+dc] == '#':
            (dr, dc) = MOVEMENT_PATTERN[(dr, dc)]
        
        r += dr
        c += dc 

    return len(seen_coords), seen_coords


def part2(positions: List[Tuple]) -> int:
    obstacle_count:int = 0
    for (o_r, o_c) in positions:
        seen_vectors:Set[Tuple[int, int, Tuple[int, int]]] = set()
        r, c, (dr, dc) = start_r, start_c, NORTH
        while True:
            if (r, c, (dr, dc)) in seen_vectors:
                obstacle_count += 1
                break

            seen_vectors.add((r, c, (dr, dc)))

            if not (0<=r+dr<H and 0<=c+dc<W):
                break
            if LAB[r+dr][c+dc] == '#' or (r+dr == o_r and c+dc == o_c):
                dr,dc = MOVEMENT_PATTERN[(dr,dc)]
            else:
                r = r+dr
                c = c+dc

    return obstacle_count


answer1, path = part1()
answer2 = part2(set(path))

print(f"""
    Part 1 = {answer1}
    Part 2 = {answer2}
""")