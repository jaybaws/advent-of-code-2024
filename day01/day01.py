from typing import List


with open("day01/input.txt", "r") as f:
    left: List[int] = list()
    right: List[int] = list()

    for (l, r) in [ l.split("   ") for l in f.readlines() ]:
        left.append(int(l))
        right.append(int(r))

    right.sort()
    left.sort()


def part1(l:List[int], r:List[int]) -> int:
    return sum(map(lambda x: abs(x[0]-x[1]), zip(l, r)))

def part2(l:List[int], r:List[int]) -> int:
    return sum(map(lambda x: x[0] * r.count(x[0]), zip(l, r)))


print(f"""
    
    Part 1 = {part1(left, right)}
    Part 2 = {part2(left, right)}

""")