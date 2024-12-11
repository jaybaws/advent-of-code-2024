from functools import cache
from typing import List


with open("day11/input.txt", "r") as f:
    I:List[int] = list(map(int, f.readline().split(" ")))


@cache
def solve(stone, steps):
    s = str(stone)
    if steps == 0:
        return 1
    elif stone == 0:
        return solve(1, steps-1)
    elif len(s) % 2 == 0:
        return solve(int(s[:len(s)//2]), steps-1) + solve(int(s[len(s)//2:]), steps-1)
    else:
        return solve(stone * 2024, steps - 1)


def part1() -> int:
    return sum(solve(stone, 25) for stone in I)


def part2() -> int:
    return sum(solve(stone, 75) for stone in I)


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")