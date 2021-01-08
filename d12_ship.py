f = open("d12_input.txt")
directions = []
for line in f:
    x = line.rstrip()
    x = [x[0],int(x[1:])]
    directions.append(x)
pos = [0,0]
cardToPos = {
    "N":[0,1],
    "S":[0,-1],
    "E":[1,0],
    "W":[-1,0]
}
rotate = ["E","S","W","N"]
face = "E"
wp = [10,1]
# for dir in directions:
#     if dir[0] == "F":
#         pos[0] += cardToPos[face][0]*dir[1]
#         pos[1] += cardToPos[face][1]*dir[1]
#     elif dir[0] == "L" or dir[0] == "R":
#         i = rotate.index(face)
#         turns = dir[1]//90
#         i = (i - turns) % len(rotate) if dir[0] == "L" else (i + turns) % len(rotate)
#         face = rotate[i]
#     else:
#         pos[0] += cardToPos[dir[0]][0]*dir[1]
#         pos[1] += cardToPos[dir[0]][1]*dir[1]
for dir in directions:
    if dir[0] == "F":
        pos[0] += wp[0]*dir[1]
        pos[1] += wp[1]*dir[1]
    elif dir[0] == "L" or dir[0] == "R":
        numTurns = dir[1]//90
        newWp = wp[:]

        i = 0 if wp[0] >= 0 else 2
        i = (i + numTurns) % len(rotate) if dir[0] == "R" else (i - numTurns) % len(rotate)

        if rotate[i] == "E" or rotate[i] == "W":
            newWp[0] = -abs(wp[0]) if rotate[i] == "W" else abs(wp[0])
        else:
            newWp[1] = -abs(wp[0]) if rotate[i] == "S" else abs(wp[0])

        i = 3 if wp[1] >= 0 else 1
        i = (i + numTurns) % len(rotate) if dir[0] == "R" else (i - numTurns) % len(rotate)

        if rotate[i] == "E" or rotate[i] == "W":
            newWp[0] = -abs(wp[1]) if rotate[i] == "W" else abs(wp[1])
        else:
            newWp[1] = -abs(wp[1]) if rotate[i] == "S" else abs(wp[1])
        wp = newWp
    else:
        wp[0] += cardToPos[dir[0]][0]*dir[1]
        wp[1] += cardToPos[dir[0]][1]*dir[1]

print(abs(pos[0])+abs(pos[1]))