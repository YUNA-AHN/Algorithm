from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        node = que.popleft()
        for nxt in graph[node]:
            if visited[nxt] == 0:
                que.append(nxt)
                visited[nxt] = 1



n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)