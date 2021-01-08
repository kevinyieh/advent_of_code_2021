from collections import deque
f = open("d9_input.txt")

nums = []
for line in f:
    cur = int(line.rstrip())
    nums.append(cur)
        
def findFirst(nums):
    queue = deque()
    available = set()
    for cur in nums:
        if len(queue) == 25:
            valid = False
            for num in queue:
                if (cur - num) != num and (cur - num) in available:
                    valid = True
                    break
            if not valid:
                return cur
            available.remove(queue.popleft())
        queue.append(cur)
        available.add(cur)


def findContiguous(nums, target):
    queue = deque()
    curSum = 0
    for num in nums:
        while curSum > target:
            curSum -= queue.popleft()
        if curSum == target:
            return queue
        curSum += num
        queue.append(num)
    return -1
            
x = findFirst(nums)
print(x)
x = findContiguous(nums,x)
print(min(x) + max(x))