def dfs(color, i, j):
    global visited, cnt
    visited[i][j] = 1
    cnt += 1

    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == color:
            dfs(color, ni, nj)


import sys
input = sys.stdin.readline
m, n = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(n)]

# 방문 체크열
visited = [[0] * m for _ in range(n)]

w_total = b_total = 0

for i in range(n):
    for j in range(m):
        # 흰색이고, 방문 이력이 없다면
        if arr[i][j] == 'W' and visited[i][j] == 0:
            cnt = 0
            dfs('W', i, j)
            w_total += cnt ** 2

        # 파란색이고, 방문 이력이 없다면
        if arr[i][j] == 'B' and visited[i][j] == 0:
            cnt = 0
            dfs('B', i, j)
            b_total += cnt ** 2

print(w_total, b_total)