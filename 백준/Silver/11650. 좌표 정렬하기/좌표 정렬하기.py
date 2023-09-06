import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]
for item in sorted(arr):
    print(*item)
