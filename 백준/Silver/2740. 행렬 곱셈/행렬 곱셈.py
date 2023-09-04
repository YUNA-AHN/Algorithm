import sys
input = sys.stdin.readline

# 행렬 a의 크기 n행 m열 / b 행렬 크기 m행 n열
n, m = map(int, input().strip().split())
a = [list(map(int, input().strip().split())) for _ in range(n)]

s, k = map(int, input().strip().split())
b = [list(map(int, input().strip().split())) for _ in range(s)]

res = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            res[i][j] += a[i][l] * b[l][j]

for item in res:
    print(*item)