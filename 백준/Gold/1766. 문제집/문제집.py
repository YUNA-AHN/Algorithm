import heapq
import sys
input = sys.stdin.readline

def topol_sort():
    que = []
    res = []
    for idx in range(1, n+1):
        if arr[idx] == 0:
            heapq.heappush(que, idx)
    while que:
        now = heapq.heappop(que)
        res.append(now)
        for nxt in graph[now]:
            arr[nxt] -= 1
            if arr[nxt] == 0:
                heapq.heappush(que, nxt)
    print(*res)

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
arr = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    arr[b] += 1

topol_sort()