from collections import deque


with open("day10/input.txt", "r") as f:
    M = [ list(map(int, [ *line.strip() ])) for line in f.readlines() ]
    H = len(M)
    W = len(M[0])
    heads = [ (r,c) for r in range(H) for c in range(W) if M[r][c] == 0 ]
    D = [ (1,0), (-1,0), (0,1), (0,-1)]


def score(grid, r, c):
    coords = deque([ (r, c) ])
    seen = { (r, c) }
    reachable_tops = 0
    while len(coords) > 0:
        cr, cc = coords.popleft()
        for nr, nc in [ (cr+dr, cc+dc) for (dr, dc) in D]:
            if (0 <= nr < H) and (0 <= nc < W) and ((nr,nc) not in seen) and (grid[nr][nc] == grid[cr][cc] + 1):
                seen.add((nr, nc))
                if grid[nr][nc] == 9:
                    reachable_tops += 1
                else:
                    coords.append((nr, nc))
    return reachable_tops


def rating(grid, r, c):
    coords = deque([(r, c)])
    seen = { (r, c): 1 }
    unique_routes = 0
    while len(coords) > 0:
        cr, cc = coords.popleft()
        if grid[cr][cc] == 9:
            unique_routes += seen[(cr, cc)]
        for nr, nc in [ (cr+dr, cc+dc) for (dr, dc) in D]:
            if (0 <= nr < H) and (0 <= nc < W) and (grid[nr][nc] == grid[cr][cc] + 1):
                if (nr, nc) in seen:
                    seen[(nr, nc)] += seen[(cr, cc)]
                else:
                    seen[(nr, nc)] = seen[(cr, cc)]
                    coords.append((nr, nc))
    return unique_routes


def part1() -> int:
    return sum(score(M, r, c) for r, c in heads)

def part2() -> int:
    return sum(rating(M, r, c) for r, c in heads)


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")