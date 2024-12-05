from typing import Tuple, List


with open("day05/input.txt", "r") as f:
    rules, updates = f.read().split("\n\n")
    rules = [ (int(x),int(y)) for (x,y) in [ r.split("|") for r in rules.splitlines() ] ]
    updates = [ list(map(int, u.split(','))) for u in updates.splitlines() ]


def is_sorted_list(update:List[int]) -> bool:
    is_valid:bool = True
    for x,y in rules:
        if x in update and y in update:
            if not(update.index(x) < update.index(y)):
                is_valid = False
                break
    return is_valid


def sortify(update:List[int]) -> List[int]:
    proceed:bool = True

    while proceed:
        proceed = False
        for x, y in rules:
            if x in update and y in update:
                px, py = update.index(x), update.index(y)
                if not(px < py):
                    update.pop(px)
                    update.insert(py, x)
                    proceed = True  # Re-check all previous moves

    return update


def solve() -> Tuple[int, int]:
    result_1, result_2 = 0, 0

    for update in updates:
        if is_sorted_list(update):
            result_1 += update[(len(update)-1) // 2]
        else:
            sortified:list = sortify(update)
            result_2 += sortified[(len(sortified)-1) // 2]

    return result_1, result_2


part1, part2 = solve()

print(f"""
   Part 1 = {part1}
   Part 2 = {part2}
""")