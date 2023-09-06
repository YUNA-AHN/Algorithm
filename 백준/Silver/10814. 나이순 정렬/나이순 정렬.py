import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [tuple(input().strip().split()) for _ in range(n)]
arr.sort(key=lambda x: int(x[0]))
for item in arr:
    print(*item)