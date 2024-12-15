import re
from math import floor


W, H = 101, 103
horizon, verizon = floor(H/2), floor(W/2)


with open("day14/input.txt", "r") as f:
    R = [ tuple(map(int, re.findall(r"\-?\d+", line))) for line in f.readlines() ]


def safety_factor(seconds:int) -> int:
    a=b=c=d=0
    for px,py,vx,vy in R:
        fx, fy = (px + (seconds*vx)) % W, (py + (seconds*vy)) % H

        if fx < verizon and fy < horizon:
            a += 1
        elif fx > verizon and fy < horizon:
            b += 1
        elif fx < verizon and fy > horizon:
            c += 1
        elif fx > verizon and fy > horizon:
            d +=1
        else:  # directly on a center-line, so omit
            pass

    return a*b*c*d

def fewest_seconds() -> int:
    min_sf = float("inf")
    best_iteration = None

    for s in range(W * H):
        sf = safety_factor(s)
        if sf < min_sf:
            min_sf = sf
            best_iteration = s
    
    return best_iteration


print(f"""
    Part 1 = {safety_factor(100)}
    Part 2 = {fewest_seconds()}
""")