from collections import defaultdict
f = open("./d7_input.txt")
outInBags = defaultdict(lambda: {})
inOutBags = defaultdict(lambda: {})

for line in f:
    line = line.rstrip()
    line = line[:-1]
    line = line.split("contain")
    outer = line[0].rstrip("s ")
    inners = line[1].rstrip()
    inners = inners.split(",")
    for inner in inners:
        inner = inner.strip("s ")
        if inner == "no other bag":
            break
        num = int(inner[0])
        innerBag = inner[2:]
        outInBags[outer][innerBag] = num
        inOutBags[innerBag][outer] = num


### Part 1
stack = []
for bag in inOutBags["shiny gold bag"]:
    stack.append(bag)
allBags = set()
while stack:
    cur = stack.pop()
    allBags.add(cur)
    for bag in inOutBags[cur]:
        stack.append(bag)
print(len(allBags))

### Part 2
def calcBags(outInBags, cur):
    total = 0
    for bag in outInBags[cur]:
        tempTotal = outInBags[cur][bag] * (calcBags(outInBags, bag)+1)
        total += tempTotal
    return total

print(calcBags(outInBags,"shiny gold bag"))