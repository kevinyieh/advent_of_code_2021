import heapq

def concurrentEvents(arr):
    arr.sort(key = lambda x: x[0])
    heap, ans = [], 0
    for intv in arr:
        start, end = intv
        if heap:
            while heap and start > heap[0]:
                heapq.heappop(heap)
        heapq.heappush(heap, end)

        ans = max(len(heap), ans)
    return ans

# x = concurrentEvents([[1,5],[2,7],[4,5],[6,10],[8,9],[9,17],[11,13],[12,15],[14,15]])
# print(x)

def search(arr):
    if not arr: return None
    l, r = 0, len(arr)-1
    while l <= r:
        m = (r+l)//2
        if arr[m] < arr[m-1]:
            return m
        elif arr[m] > arr[l] or arr[m] > arr[r]:
            l = m + 1
        elif arr[m] < arr[r] or arr[m] < arr[l]:
            r = m - 1
        else:
            l,r = l+1, r-1
x = search([1,1,1,2,1,1,1,1,1,1,1,1,1,1,1])
print(x)