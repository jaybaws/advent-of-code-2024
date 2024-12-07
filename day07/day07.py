from typing import Callable, List, Tuple


def parse_equation(line:str) -> Tuple[int, List[int]]:
    left, right = line.split(': ')
    return int(left), list(map(int, right.split(' ')))

with open("day07/input.txt", "r") as f:
    equations = [ parse_equation(line) for line in f.readlines() ]

def add(a:int, b:int) -> int:
    return a + b

def multiply(a:int, b:int) -> int:
    return a * b

def concatenate(a:int, b:int) -> int:
    return int(str(a)+str(b))

def is_solvable(parts:List[int], desired_result:int, intermediate_result:int, operations:List[Callable]) -> bool:
    if len(parts) == 0:
        return intermediate_result == desired_result
    else:
        next_part:int = parts[0]
        computations = [ o(intermediate_result, next_part) for o in operations ] 
        return any([ is_solvable(parts[1:], desired_result, c, operations) for c in computations ])

def solve(operations:List[Callable]) -> int:
    total_calibration_result:int = 0
    for (desired_result, parts) in equations:
        if is_solvable(parts[1:], desired_result, parts[0], operations):
            total_calibration_result += desired_result
    return total_calibration_result

print(f"""
    Part 1 = {solve([ add, multiply ])}
    Part 2 = {solve([ add, multiply, concatenate ])}
""")