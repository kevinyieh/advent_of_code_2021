f = open("d10_input.txt")
arr = []
for line in f:
    arr.append(int(line.rstrip()))

def part1(arr):
    diffs = {1:0, 3:0}
    arr.sort()
    prev = 0
    for jolt in arr:
        d = jolt-prev
        if d > 3: break
        if jolt-prev in diffs:
            diffs[jolt-prev] += 1
        prev = jolt
    return diffs

x = part1(arr)
print(x[1]*(x[3]+1))
phone = max(arr)+3
seen = {}
def part2(arr,prev, idx):
    global seen, phone
    nxtPossible = []
    while idx < len(arr):
        if arr[idx]-prev <= 3:
            nxtPossible.append([arr[idx],idx])
        else:
            break
        idx += 1
    if not nxtPossible:
        return 0 if phone-prev > 3 else 1
    total = 0
    for cur,idx in nxtPossible:
        temp = seen[cur] if cur in seen else part2(arr, cur, idx+1) 
        seen[cur] = temp
        total += temp
    return total

print(part2(arr,0,0))