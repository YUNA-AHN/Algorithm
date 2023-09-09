import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
# 우선순위 큐 이용
que = []
for i in range(n):
    num = int(input().strip())
    heapq.heappush(que, num)

for _ in range(n):
    print(heapq.heappop(que))