from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    global visited
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    while que:
        i, j = que.popleft()
        for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                que.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]

bfs(0,0)
print(visited[n-1][m-1])