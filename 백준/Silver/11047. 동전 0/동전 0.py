import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = [int(input()) for _ in range(n)]

total = 0
for i in range(n-1, -1, -1):
    if k >= arr[i]:
        total += k // arr[i]
        k %= arr[i]
print(total)
