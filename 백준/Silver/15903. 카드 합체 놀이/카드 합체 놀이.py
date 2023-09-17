import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().strip().split())
arr = sorted(list(map(int, input().strip().split())))

for _ in range(m):
    num1 = heapq.heappop(arr)
    num2 = heapq.heappop(arr)
    plus = num1 + num2
    heapq.heappush(arr, plus)
    heapq.heappush(arr, plus)

print(sum(arr))