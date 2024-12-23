nodes = {}
for a, b in [ line.strip().split('-') for line in open("day23/input.txt", "r").readlines() ]:
    if a not in nodes:
        nodes[a] = list([b])
    else:
        nodes[a].append(b)
    
    if b not in nodes:
        nodes[b] = list([a])
    else:
        nodes[b].append(a)


def part1() -> int:
    sets = set()
    for a in nodes:
        for b in nodes[a]:
            for c in nodes[b]:
                if a != c and a in nodes[c]:
                    if ",t" in f",{a},{b},{c}":
                        sets.add(tuple(sorted([a, b, c])))
    return len(sets)


def part2() -> int:
    sets = set()
    
    def search(node, req):
        key = tuple(sorted(req))
        if key in sets:
            return
        else:
            sets.add(key)
       
        for neighbor in nodes[node]:
            if neighbor in req or not all(neighbor in nodes[query] for query in req):
                continue
            else:
                search(neighbor, {*req, neighbor})

    for x in nodes:
        search(x, {x})

    return ",".join(sorted(max(sets, key=len)))


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")