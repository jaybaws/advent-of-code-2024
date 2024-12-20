with open("day20/input.txt", "r") as f:  # Read the map
    I = [ [ *line ] for line in f.read().splitlines() ]
    H = len(I)
    W = len(I[0])

# Find the start, end and track positions
track = set()
for r in range(H):
    for c in range(W):
        if I[r][c] == "S":
            start_r, start_c = r, c
        elif I[r][c] == "E":
            end_r, end_c = r, c
        elif I[r][c] == ".":
            track.add((r,c))

# Determine the single path of track positions (and the respective distance of each track position)
r, c, d = start_r, start_c, 0
path = { (r, c): d }
while (r, c) != (end_r, end_c):
    # Find any neighbour (east,west,south,noth) which is track/finish and is not yet already on the path.
    for nr, nc in [ (r+dr, c+dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)] if ((r+dr,c+dc) == (end_r, end_c) or (r+dr,c+dc) in track) and (r+dr,c+dc) not in path ]:
        d += 1
        path[(nr, nc)] = d
        r,c = nr, nc

# Find shortcuts
def find_cheats(max_cheat_duration:int, minimal_desired_saving:int) -> int:
    total = 0
    for r,c in path.keys():
        d = path[(r,c)]

        # Find all other track positions within maximum allowed (manhattan) distance.
        # As these positions could be already behind you, we only care about those whose saving equals/exceeds the desired saving!
        for _ in [ (nr, nc) for nr,nc in path.keys() if abs(nr-r)+abs(nc-c) <= max_cheat_duration and path[(nr,nc)] - d - (abs(nr-r)+abs(nc-c)) >= minimal_desired_saving]:
            total += 1

    return total

print(f"""
    Part 1 = {find_cheats(2, 100)}
    Part 2 = {find_cheats(20, 100)}
""")