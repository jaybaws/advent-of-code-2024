import heapq


MAZE = [ list(line.strip()) for line in open("day16/input.txt", "r") ]
H, W = len(MAZE), len(MAZE[0])
for r in range(H):
    for c in range(W):
        if MAZE[r][c] == "S":
            start_r = r
            start_c = c


def part1() -> int:
    prioqueue, seen = [ (0, start_r, start_c, 0, 1) ], { (start_r, start_c, 0, 1) }

    while prioqueue:
        cost, r, c, dr, dc = heapq.heappop(prioqueue)
        if MAZE[r][c] == "E":
            return cost
        else:
            seen.add((r, c, dr, dc))
            for new_cost, next_r, next_c, next_dr, next_dc in [ (cost + 1, r+dr, c+dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr) ]:
                if MAZE[next_r][next_c] != "#" and (next_r, next_c, next_dr, next_dc) not in seen:
                    heapq.heappush(prioqueue, (new_cost, next_r, next_c, next_dr, next_dc))


def part2() -> int:
    return None


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")