f = open("./d17_input.txt")
mat = []
for line in f:
    mat.append(list(line.strip()))

cubes = set()
for x in range(len(mat)):
    for y in range(len(mat[x])):
        if mat[x][y] == "#":
            cubes.add((x,y,0,0))

def neighbors(x,y,z,w):
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            for dz in (-1,0,1):
                for dw in (-1,0,1):
                    if dx == dy == dz == dw == 0: continue
                    yield (x+dx,y+dy,z+dz,w+dw)

def countActive(p):
    count = 0
    for n in neighbors(*p):
        if n in cubes: count += 1
    return count

def step():
    nextCubes = set()
    for p in cubes:
        if countActive(p) in (2,3):
            nextCubes.add(p)
        for n in neighbors(*p):
            count = countActive(n) 
            if n not in cubes and count == 3:
                nextCubes.add(n)
            elif n in cubes and count in (2,3):
                nextCubes.add(n)
    return nextCubes

for _ in range(6):
    cubes = step()

print(len(cubes))