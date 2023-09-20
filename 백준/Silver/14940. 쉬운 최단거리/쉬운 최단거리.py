'''
최단거리
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
que = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            que.append((i,j))
            while que:
                k, l = que.popleft()
                for dk, dl in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nk, nl = k + dk, l + dl
                    if 0 <= nk < n and 0 <= nl < m and visited[nk][nl] == 0 and arr[nk][nl] == 1:
                        que.append((nk, nl))
                        visited[nk][nl] += visited[k][l] + 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
                        
for r in range(n):
    print(*visited[r])