nums = [ int(line) for line in open("day22/input.txt", "r") ]

def calc(x):
    x = (x ^ (x * 64)) % 16777216
    x = (x ^ (x // 32)) % 16777216
    x = (x ^ (x * 2048)) % 16777216
    
    return x


def part1() -> int:
    total = 0

    for num in nums:
        for _ in range(2000):
            num = calc(num)
        total += num
    
    return total

def part2() -> int:
    seq_to_total = {}

    for num in nums:
        buyer = [ num % 10 ]
        for _ in range(2000):
            num = calc(num)
            buyer.append(num % 10)

        seen = set()
        for i in range(len(buyer) - 4):
            a, b, c, d, e = buyer[i:i + 5]
            seq = (b - a, c - b, d - c, e - d)
            if seq in seen:
                continue

            seen.add(seq)
            if seq not in seq_to_total:
                seq_to_total[seq] = 0

            seq_to_total[seq] += e

    return max(seq_to_total.values())


print(f"""
    Part 1 = {part1()}
    Part 2 = {part2()}
""")