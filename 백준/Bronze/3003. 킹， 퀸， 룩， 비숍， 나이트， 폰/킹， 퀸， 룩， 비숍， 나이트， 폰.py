import sys
input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().strip().split()))

for i in range(len(chess)):
    chess[i] -= arr[i]

print(*chess)