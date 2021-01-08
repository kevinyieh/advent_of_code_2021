f = open("./d8_input.txt")
arr = []
for line in f:
    line = line.rstrip()
    line = line.split(" ")
    line[1] = int(line[1]) if line[1][0] == "-" else int(line[1][1:])
    arr.append(line)

j = 0
i = 0
while i < len(arr) and j < len(arr):
    seen = set()
    acc = i = 0
    while j < len(arr):
        if arr[j][0] == "nop":
            arr[j][0] = "jmp"
            j += 1
            break
        elif arr[j][0] == "jmp":
            arr[j][0] = "nop"
            j += 1
            break
        j += 1
    while i < len(arr):
        if i in seen:
            i = 0
            arr[j-1][0] = "jmp" if arr[j-1][0] == "nop" else "nop"
            break
        prev = i
        act, num = arr[i]
        if act == "acc":
            acc += num
        elif act == "jmp":
            i += num - 1
        seen.add(i)
        
        i += 1
print(acc)