from functools import cache


with open("day19/input.txt", "r") as f:
    lines = f.read().splitlines()
    patterns = set(lines[0].split(", "))
    max_length = max(map(len, patterns))
    designs = lines[2:]

@cache
def possibilities(design):
    if design == "":
        return 1
    count = 0
    for i in range(min(len(design), max_length) + 1):
        if design[:i] in patterns:
            count += possibilities(design[i:])
    return count


def part1() -> int:
    return sum(possibilities(design) > 0 for design in designs)

def part2() -> int:
    return sum(possibilities(design) for design in designs)


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")