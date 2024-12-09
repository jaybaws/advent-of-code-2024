from typing import Dict, List, Tuple


disk_map:List[List[int]] = []
files:Dict[int, Tuple[int, int]] = {}
free_space:List[Tuple[int, int]] = list()
location:int = 0

for i, char in enumerate(open("day09/input.txt", "r").read()):
    size:int = int(char)

    if i % 2 == 0:
        disk_map += [ i // 2 ] * size
        files[i // 2] = (location, size)
    else:
        disk_map += [ None ] * size
        free_space.append((location, size))

    location += size


def part1() -> int:
    global disk_map

    for i in [ i for i, x in enumerate(disk_map) if x == None ]:
        while disk_map[-1] == None:
            disk_map.pop()
        
        if len(disk_map) <= i:
            break
        
        disk_map[i] = disk_map.pop()

    return sum([ i * x for i, x in enumerate(disk_map) ])


def part2() -> int:
    global free_space

    id: int = max(files.keys())
    while id > 0:
        position, size = files[id]
        for i, (start, length) in enumerate(free_space):
            if start >= position:
                free_space = free_space[:i]
                break
            if size <= length:
                files[id] = (start, size)
                if size == length:
                    free_space.pop(i)
                else:
                    free_space[i] = (start + size, length - size)
                break
        id -= 1


    total = 0
    for id, (position, size) in files.items():
        for x in range(position, position + size):
            total += id * x

    return total


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")