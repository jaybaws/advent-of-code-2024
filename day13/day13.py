import re


def solve(increase:int=0) -> int:
    total = 0
    with open("day13/input.txt", "r") as input:
        for machine in input.read().split("\n\n"):
            x_a, y_a, x_b, y_b, x_prize, y_prize = map(int, re.findall(r"\d+", machine))
            x_prize += increase
            y_prize += increase    
            ca = (x_prize * y_b - y_prize * x_b) / (x_a * y_b - y_a * x_b)
            cb = (x_prize - x_a * ca) / x_b
            if (ca % 1 == 0) and (cb % 1 == 0):
                if (increase > 0) or (ca <= 100 and cb <= 100):
                    total += int(ca * 3 + cb)
    return total


print(f"""
    Part 1 = {solve()}
    Part 2 = {solve(10000000000000)}
""")