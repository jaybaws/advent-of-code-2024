with open("day04/input.txt", "r") as f:
    puzzle = [ [ char for char in line.strip() ] for line in f.readlines() ]
    height = len(puzzle)
    width = len(puzzle[0])
    ALL_DIRECTIONS = [ (0, 1), (1, 1), (1, 0), (1, -1),(0, -1), (-1, -1), (-1, 0), (-1, 1) ]
    VALID_MAS = [ 'MS', 'SM' ]

def part1() -> int:
    count:int = 0
    for r in range(height):
        for c in range(width):
            if puzzle[r][c] == 'X':
                for (dr, dc) in ALL_DIRECTIONS:
                    if 0 <= r+(3*dr) <= (height-1) and 0<= c+(3*dc) <= (width-1):
                        if puzzle[r+(1*dr)][c+(1*dc)] == 'M' and puzzle[r+(2*dr)][c+(2*dc)] == 'A' and puzzle[r+(3*dr)][c+(3*dc)] == 'S':
                            count += 1
    return count

def part2() -> int:
    count:int = 0
    for r in range(1, height-1):
        for c in range(1,width-1):
            if puzzle[r][c] == 'A':
                nw2se = f"{puzzle[r-1][c-1]}{puzzle[r+1][c+1]}"
                ne2sw = f"{puzzle[r-1][c+1]}{puzzle[r+1][c-1]}"
                if nw2se in VALID_MAS and ne2sw in VALID_MAS:
                    count += 1
    return count

print(f"""
   Part 1 = {part1()}.
   Part 2 = {part2()}.
""")