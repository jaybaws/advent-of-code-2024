from typing import List
from copy import deepcopy

with open("day02/input.txt", "r") as f: I = [ [ int(x) for x in line.split() ] for line in f.read().splitlines() ]

def is_safe_1(report: List[int]) -> bool:
    increasing:bool = report[1] > report[0]
    for i in range(1, len(report)):
        if (report[i] > report[i-1]) != increasing or abs(report[i]-report[i-1]) not in [1, 2, 3]:
            return False

    return True


def is_safe_2(report: List[int]) -> bool:
    if is_safe_1(report):
        return True
    
    for i in range(len(report)):
        new_report = deepcopy(report)
        del new_report[i]
        if is_safe_1(new_report):
            return True


print(f"""
      Part 1 = {len([report for report in I if is_safe_1(report)])}
      Part 2 = {len([report for report in I if is_safe_2(report)])}
""")