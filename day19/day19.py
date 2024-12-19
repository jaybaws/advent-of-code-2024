from functools import cache


with open("day19/input.txt", "r") as f:
    lines = f.read().splitlines()
    patterns = set(lines[0].split(", "))
    maxlen = max(map(len, patterns))


@cache
def possibilities(pattern):
    if pattern == "":
            return 1
    count = 0
    for i in range(min(len(pattern), maxlen) + 1):
        if pattern[:i] in patterns:
            count += possibilities(pattern[i:])
    return count


def part1() -> int:
    return sum(possibilities(design) > 0 for design in lines[2:])

def part2() -> int:
    return sum(possibilities(design) for design in lines[2:])


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")