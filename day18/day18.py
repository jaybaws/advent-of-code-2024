from collections import deque


I = [ list(map(int, line.split(","))) for line in open("day18/input.txt", "r") ]


def shortest_distance_to_exit(num_bytes:int = 1024) -> int:
    memory_size, corrupted = 70, []
    for c, r in I[:num_bytes]:
        corrupted.append((r,c))

    q, seen = deque([ (0, 0, 0) ]), { (0, 0) }
    while q:
        r, c, distance = q.popleft()
        for nr, nc in [ (r+1, c), (r, c+1), (r-1, c), (r, c-1)] :
            if (0 <= nr <= memory_size) and (0 <= nc <= memory_size) and (nr, nc) not in seen and (nr, nc) not in corrupted: 
                if nr == nc == memory_size:
                    return distance + 1
                
                seen.add((nr, nc))
                q.append((nr, nc, distance + 1))

    return None


def part2():
    left, right = 0, len(I) - 1
    while left < right:
        middle = (left + right) // 2
        if shortest_distance_to_exit(middle + 1) is not None:
            left = middle + 1
        else:
            right = middle

    return f"{I[left][0]},{I[left][1]}"


print(f"""
    Part 1 = {shortest_distance_to_exit()}
    Part 2 = {part2()}
""")