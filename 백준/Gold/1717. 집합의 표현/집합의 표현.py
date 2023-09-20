import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return
    if px < py:
        parents[parents[y]] = x
    else:
        parents[parents[x]] = y

n, m = map(int, input().strip().split())
parents = [i for i in range(n+1)]
for _ in range(m):
    oper, a, b = map(int, input().strip().split())
    if oper == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')