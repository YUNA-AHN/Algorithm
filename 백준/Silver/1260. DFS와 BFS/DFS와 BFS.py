from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    visited_d[v] = 1
    print(v, end=' ')
    for u in arr[v]:
        if visited_d[u] == 0:
            dfs(u)

def bfs(v):
    que = deque()
    que.append(v)
    visited_b[v] = 1
    while que:
        u = que.popleft()
        print(u, end=' ')
        for i in arr[u]:
            if visited_b[i] == 0:
                que.append(i)
                visited_b[i] = 1

n, m ,v = map(int, input().strip().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    arr[b].append(a)
    arr[a].append(b)

for i in range(n+1):
    arr[i].sort()

visited_d = [0] * (n+1)
dfs(v)
print()

visited_b = [0] * (n+1)
bfs(v)
print()
