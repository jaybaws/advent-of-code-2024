import re


output = []
pointer = 0
A, B, C, *program = list(map(int, re.findall(r"\d+", open("day17/input.txt",  "r").read())))


def value_of(combo_operand: int) -> int:
    global A, B, C
    match combo_operand:
        case 4: return A
        case 5: return B
        case 6: return C
        case _: return combo_operand

def adv(combo_operand: int):
    global A
    A = int(A / (2 ** value_of(combo_operand)))

def bxl(literal_operand: int):
    global B
    B ^= literal_operand

def bst(combo_operand: int):
    global B
    B = value_of(combo_operand) % 8

def jnz(literal_operand):
    global A, pointer
    if A != 0: pointer = literal_operand -2

def bxc(_: int):
    global B, C
    B ^= C

def out(combo_operand: int):
    global output
    output.append(str(int(value_of(combo_operand) % 8)))

def bdv(combo_operand: int):
    global A, B
    B = int(A / (2 ** value_of(combo_operand)))

def cdv(combo_operand: int):
    global A, C
    C = int(A / (2 ** value_of(combo_operand)))

operations = { 0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv }

while pointer < len(program):
    opcode, operand = program[pointer], program[pointer+1]
    operation = operations[opcode]
    _ = operation(operand)
    pointer += 2

part1:str = ",".join(output)

print(f"""
    Part 1 = {part1}
""")