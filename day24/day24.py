from collections import deque

def f_and(a:int, b:int) -> int:
    return a & b

def f_or(a:int, b:int) -> int:
    return a | b

def f_xor(a:int, b:int) -> int:
    return a ^ b

ops = { "AND": f_and, "OR": f_or, "XOR": f_xor }


with open("day24/input.txt", "r") as f:
    init_values, init_formulas = f.read().split("\n\n")
    values = { k:int(v) for (k,v) in [ l.split(": ") for l in init_values.splitlines() ] }
    formulas = [ f.replace(" -> ", " ").split() for f in init_formulas.splitlines() ]


def part1() -> int:
    q = deque(formulas)
    while q:
        formula = q.popleft()
        a, op, b, out = formula
        if a in values and b in values:
            result = ops[op](values[a], values[b])
            values[out] = result
        else:
            q.append(formula)

    i, bin = 0, ""
    while True:
        key = "z" + str(i).rjust(2, "0")
        if key not in values:
            break
        bin += str(int(values[key]))
        i += 1
    
    return int(bin[::-1], 2)


def part2() -> int:
    return None

print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")