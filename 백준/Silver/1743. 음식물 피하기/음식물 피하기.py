import sys
sys.setrecursionlimit(10000) 

def dfs(x, y):
    global cnt, visited
    visited[x][y] = 1
    cnt += 1

    for di, dj in [[0,1], [0,-1], [1,0],[-1,0]]:
        ni = x + di
        nj = y + dj
        if 0 <= ni < n+1 and 0 <= nj < m+1 and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            dfs(ni, nj)

n, m, k = map(int, input().split())
arr = [[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
    i, j = map(int, input().split())
    arr[i][j] = 1

visited = [[0] * (m+1) for _ in range(n+1)]

mx = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt = 0
        if visited[i][j] == 0 and arr[i][j] == 1:
            dfs(i, j)
            mx = max(cnt, mx)
print(mx)
