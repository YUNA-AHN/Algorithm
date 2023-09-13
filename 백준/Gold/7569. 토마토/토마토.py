# 토마토
from collections import deque
import sys
input = sys.stdin.readline

# bfs
def bfs():
    global mn
    while que:
        i, j, k = que.popleft()
        # 상하좌우위아래 체크 범위내라면 que에 입력,
        for di, dj, dk in [[0,0,1], [0, 0, -1], [0,1,0], [0, -1, 0], [-1,0,0], [1,0,0]]:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m and arr[ni][nj][nk] == 0 and visited[ni][nj][nk] == 0:
                # arr[ni][nj][nk] = 1
                que.append((ni,nj,nk))
                visited[ni][nj][nk] = visited[i][j][k] + 1


# 열, 행, 높이
m, n, h = map(int, input().strip().split())
arr = [[list(map(int, input().strip().split())) for _ in range(n)] for k in range(h)]

visited = [[[0]*m for _ in range(n)] for _ in range(h)]

# 익은 토마토들 동시에 돌리기 위해 미리 que에 입력, 방문 체크열에도 체크
que = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                que.append((i, j, k))
                visited[i][j][k] = 1

bfs()

ans = 0
# 0있는지 확인 있으면 -1 출력, 있으면 최고값-1 출력
for i in range(h):
    for j in range(n):
        for k in range(m):
            if visited[i][j][k] == 0 and arr[i][j][k] == 0:
                ans = -1
                break
            else:
                ans = max(ans, visited[i][j][k]-1)
        if ans == -1:
            break
    if ans == -1:
        break

print(ans)
