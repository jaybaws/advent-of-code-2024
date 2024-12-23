from collections import deque


with open("day12/input.txt", "r") as f:
    D = [ (1,0), (-1,0), (0,1), (0,-1) ]
    M = [ [*line.strip()] for line in f.readlines() ]
    H = len(M)
    W = len(M[0])


def solve() -> int:
    seen = set()
    total_price_1 = total_price_2 = 0

    for r in range(H):
        for c in range(W):
            if (r, c) not in seen:
                seen.add((r, c))
                region = set([ (r, c) ])
                sides = list()
                q = deque([ (r, c) ])

                while q:
                    cr, cc = q.popleft()
                    for nr, nc in [ (cr+dr,cc+dc) for dr,dc in D if (cr+dr,cc+dc) not in region ]:
                        if not((0 <= nr < H) and (0 <= nc < W)) or M[nr][nc] != M[r][c]:
                            sides.append((r, c))
                        else:
                            q.append((nr, nc))
                            region.add((nr, nc))
                            seen.add((nr, nc))

                total_price_1 += len(region) * len(sides)
                # surrounding = [ (pr+dr, pc+dc) for pr,pc in sides for dr,dc in D if (pr+dr,pc+dc) not in region ]
                # and then what?
                
                # total_price_2 += len(region) * len(???)


    return total_price_1, total_price_2

part1, part2 = solve()

print(f"""
    Part 1 = {part1}
    Part 2 = {part2}
""")