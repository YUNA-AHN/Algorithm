import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(range(n+1))
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    arr[i], arr[j] = arr[j], arr[i]
print(*arr[1:])