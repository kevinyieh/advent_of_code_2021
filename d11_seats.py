f = open("d11_input.txt","r")
mat = []
for line in f:
    mat.append([x for x in line.rstrip()])

dirs = [[1,0],[1,1],[1,-1],
        [0,1],[0,-1],
        [-1,0],[-1,1],[-1,-1]]

def noOccupiedAdj(mat,pos):
    global dirs
    for dir in dirs:
        if look(mat,dir,pos) == "#":
            return False
    return True

def surrounded(mat,pos):
    global dirs
    occupancy = 0
    for dir in dirs:
        if look(mat,dir,pos) == "#":
            occupancy += 1
        if occupancy >= 5:
            return True
    return False

def look(mat,dir,pos):
    r, c = [pos[0]+dir[0], pos[1]+dir[1]]
    while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        if mat[r][c] == "#" or mat[r][c] == "L":
            return mat[r][c] 
        r += dir[0]
        c += dir[1]
    return "."

def changeSeat(mat,pos):
    r,c = pos
    mat[r][c] = "#" if mat[r][c] == "L" else "L"

changeOccured = True
while changeOccured:
    changeOccured = False
    posToChange = []
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == "L" and noOccupiedAdj(mat,[r,c]) :
                posToChange.append([r,c])
                changeOccured = True
            if mat[r][c] == "#" and surrounded(mat,[r,c]):
                posToChange.append([r,c])
                changeOccured = True
    for pos in posToChange:
        changeSeat(mat,pos)

occupiedSeats = 0
for row in mat:
    for x in row:
        if x == "#":
            occupiedSeats+=1
print(occupiedSeats)