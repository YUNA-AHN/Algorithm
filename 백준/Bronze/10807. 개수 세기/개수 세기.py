import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

cnt = 0
for i in range(n):
    if arr[i] == k:
        cnt += 1

print(cnt)