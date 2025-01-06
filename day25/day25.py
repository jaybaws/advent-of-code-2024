with open("day25/input.txt", "r") as f:
    parts = f.read().split("\n\n")
    keys, locks = [ part for part in parts if part[0:5] == "#####" ], [ part for part in parts if part[0:5] == "....." ]

total = 0
for l in locks:
    for k in keys:
        lock, key = l.splitlines(), k.splitlines()

        fits = True
        for c in range(5):
            for r in range(7):
                if lock[r][c] == "#" and key[r][c] == "#":
                    fits = False
        if fits:
            total += 1

print(total)