D = { "<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0) }


walls = list()
boxes = list()
start_r = start_c = None


def display(robot_r, robot_c, header="Initial state:"):
    end = (robot_r,robot_c)
    print(f"\n{header}")
    for r in range(H):
        line = ""
        for c in range(W):
            if (r,c) == end:
                line += "@"
            elif (r,c) in walls:
                line += "#"
            elif (r,c) in boxes:
                line += "O"
            else:
                line += "."

        print(line)


with open("day15/input.txt", "r") as f:
    layout, moves = f.read().split("\n\n")
    for r, line in enumerate(layout.splitlines()):
        for c, obj in enumerate(line):
            if obj == '@':
                start_r, start_c = r, c
            elif obj == '#':
                walls.append((r, c))
            elif obj == 'O':
                boxes.append((r, c))
            else:
                pass

    H = r + 1
    W = c + 1

    moves = [ move for move in moves.replace("\n", "")]
    

r, c = start_r, start_c
# display(r,c)

for move in moves:
    dr, dc = D.get(move)
    dest = (r+dr, c+dc)
    
    if dest in walls:
        pass
    elif dest not in boxes:
        r, c = dest  # move into the free '.'
    else:
        boxes_to_move = []
        can_move = None
        br,bc = r, c
        while True:
            br += dr
            bc += dc
            if (br,bc) in boxes:
                boxes_to_move.append((br,bc))
                continue
            elif (br,bc) in walls:
                can_move = False
                break
            else:  # must be '.' free space
                can_move = True
                break

        if can_move:
            r, c = dest  # Move into the place of the box
            for (br, bc) in boxes_to_move:  # Remove all boxes
                boxes.remove((br,bc))
            for (br, bc) in boxes_to_move:  # Re-add the boxes in their new places
                boxes.append((br+dr,bc+dc))

    # display(r,c, f"Move {move}:")

print(sum([ 100*r + c for r,c in boxes]))
