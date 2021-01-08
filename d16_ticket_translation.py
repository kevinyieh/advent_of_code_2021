f = open("./d16_input.txt")
input = [{},[],[]]
i = 0
for line in f:
    if line == "\n": 
        i += 1
        continue
    if i == 0:
        line = [x.strip() for x in line.split(":")]
        key = line[0]
        ranges = [x.strip().split("-") for x in line[1].split("or")]
        ranges = [(int(y),int(z)) for y,z in ranges]
        input[i][key] = ranges
    elif i == 1:
        if line.strip() == "your ticket:": continue
        input[i] = [int(x) for x in line.strip().split(",")]
    else:
        if line.strip() == "nearby tickets:": continue
        input[i].append([int(x) for x in line.strip().split(",")])
mn = float('inf')
mx = float('-inf')
for range1, range2 in input[0].values():
    mn = min(range1[0],mn)
    mx = max(range2[1],mx)
invalid = set(list(range(mn,mx)))

for range1, range2 in input[0].values():
    invalid -= set(list(range(range1[0],range1[1]+1)))
    invalid -= set(list(range(range2[0],range2[1]+1)))

# errorRate = 0

# for ticket in input[2]:
#     for num in ticket:
#         if num in invalid or num < mn or num > mx:
#             errorRate += num
# print(errorRate)

validTickets = []
for ticket in input[2]:
    valid = True
    for num in ticket:
        if num in invalid or num < mn or num > mx:
            valid = False
            break
    if valid:
        validTickets.append(ticket)
index = input[0]
fields = [set(list(index.keys())) for _ in index.keys()]

for ticket in validTickets:
    for i in range(len(ticket)):
        val = ticket[i]
        remove = []
        for key in fields[i]:
            lower, upper = index[key]
            if lower[1] < val < upper[0]:
                remove.append(key)
        for key in remove:
            fields[i].remove(key)

correct = 0
correctFields = [None]*len(fields)
seen = set()
while correct != len(fields):
    rem = None
    for i in range(len(fields)):
        if len(fields[i]) == 1:
            rem = fields[i].pop()
            correctFields[i] = rem
            correct += 1
    if rem:
        for field in fields:
            if rem in field:
                field.remove(rem)
print(correctFields)
total = 1

for i in range(len(correctFields)):
    if correctFields[i].split(" ")[0] == "departure":
        total *= input[1][i]

print(total)