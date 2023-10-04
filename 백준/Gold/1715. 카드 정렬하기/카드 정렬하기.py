import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
total = 0

for _ in range(n):
    num = int(input())
    heapq.heappush(arr, num)


for _ in range(n-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    total += a+b
    heapq.heappush(arr, a+b)

print(total)