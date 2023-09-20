'''
적록색약
R, G=B/ R, G, B
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs_n(v,color):
    que = deque()
    que.append(v)
    while que:
        k, l = que.popleft()
        for dk, dl in [[0,1],[0,-1],[1,0],[-1,0]]:
            nk, nl = k + dk , l + dl
            if 0 <= nk < n and 0 <= nl < n and visited_n[nk][nl] == 0 and arr[nk][nl] == color:
                que.append((nk,nl))
                visited_n[nk][nl] = 1

def bfs_v(v,color):
    que = deque()
    que.append(v)
    while que:
        k, l = que.popleft()
        if color == 'B':
            for dk, dl in [[0,1],[0,-1],[1,0],[-1,0]]:
                nk, nl = k + dk , l + dl
                if 0 <= nk < n and 0 <= nl < n and visited_v[nk][nl] == 0 and arr[nk][nl] == color:
                    que.append((nk,nl))
                    visited_v[nk][nl] = 1
        else:
            for dk, dl in [[0,1],[0,-1],[1,0],[-1,0]]:
                nk, nl = k + dk , l + dl
                if 0 <= nk < n and 0 <= nl < n and visited_v[nk][nl] == 0 and arr[nk][nl] != 'B':
                    que.append((nk,nl))
                    visited_v[nk][nl] = 1

n = int(input().strip())
arr = [list(input().strip()) for _ in range(n)]

visited_n = [[0] * n for _ in range(n)]
visited_v = [[0] * n for _ in range(n)]
cnt_n = cnt_r = 0
for i in range(n):
    for j in range(n):
        if visited_n[i][j] == 0:
            visited_n[i][j] = 1
            bfs_n((i,j), arr[i][j])
            cnt_n += 1

        if visited_v[i][j] == 0:
            visited_v[i][j] = 1
            bfs_v((i, j), arr[i][j])
            cnt_r += 1

print(cnt_n, cnt_r)
