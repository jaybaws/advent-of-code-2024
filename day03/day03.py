import re

with open("day03/input.txt", "r") as f: I = f.read()

pattern_part1 = r"mul\(\d{1,3},\d{1,3}\)"
pattern_part2 = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))"

def compute(input: str) -> int:
    a, b = map(int, input.removeprefix("mul(").removesuffix(")").split(","))
    return a * b

def part1() -> int:
    return sum(map(compute, re.findall(pattern_part1, I)))

def part2() -> int:
    do_it: bool = True
    result: int = 0
    
    for instruction in re.findall(pattern_part2, I):
        if instruction == "do()":
            do_it = True
        elif instruction == "don't()":
            do_it = False
        else:
            if do_it:
                result += compute(instruction)

    return result

print(f"""
   Part 1 = {part1()}   
   Part 2 = {part2()}
""")