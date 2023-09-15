# 상범 빌딩
from collections import deque
import sys
input = sys.stdin.readline

# 층, 행, 열
while True:
    l, r, c = map(int, input().strip().split())

    if l == r == c == 0:
        break

    arr = [[list(input().strip()) for _ in range(r)]]
    for _ in range(l-1):
        blank = input()
        arr.append([list(input().strip()) for _ in range(r)])
    blank = input()

    que = deque()
    ei, ej, ek = 0, 0, 0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    que.append((i,j,k))
                    arr[i][j][k] = 1
                elif arr[i][j][k] == '#':
                    arr[i][j][k] = 1
                elif arr[i][j][k] == 'E':
                    arr[i][j][k] = 0
                    ei, ej, ek = i, j, k
                else:
                    arr[i][j][k] = 0

    while que:
        i, j, k = que.popleft()
        for di, dj, dk in[[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < l and 0 <= nj < r and 0 <= nk < c and arr[ni][nj][nk] == 0:
                que.append((ni,nj,nk))
                arr[ni][nj][nk] = arr[i][j][k] + 1

    if arr[ei][ej][ek]:
        print(f'Escaped in {arr[ei][ej][ek]-1} minute(s).')
    else:
        print('Trapped!')