n, m = map(int, input().split())
arr = list(range(n+1))

for _ in range(m):
    i, j = map(int, input().split())
    for k in range((j-i) // 2 + 1):
        arr[j - k], arr[i + k] = arr[i + k], arr[j - k]

print(*arr[1:])