input = [14,3,1,0,9,5]
lastSpoken = {x:i+1 for i,x in enumerate(input[:-1])}
i, prev = len(input),input[-1]

while i < 30000000:
    nxtNumber = 0 if prev not in lastSpoken else i-lastSpoken[prev]
    lastSpoken[prev], prev = i, nxtNumber
    i += 1
print(prev)

# def part2(arr):
#     spoken = dict()
#     for num in arr:
#         spoken[num] = arr.index(num)
#     del spoken[arr[-1]]
#     curr_index = len(arr)-1
#     while curr_index != 299999999:
#         last_spoken = arr[curr_index]
#         if last_spoken in spoken:
#             arr.append(curr_index-spoken[last_spoken])
#         else:
#             arr.append(0)
#         spoken[last_spoken]=curr_index
#         curr_index+=1
#     return arr[-1]
# print(part2(input))