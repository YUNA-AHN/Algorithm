def graphs(p):
    global i
    if p <= n:
        graphs(p*2)
        i += 1
        tree[p-1] = arr[i]
        graphs(p * 2 + 1)

import sys
input = sys.stdin.readline

k = int(input().strip())
arr = list(map(int, input().strip().split()))
n = len(arr)
tree = [0] * n
i = -1
graphs(1)

s = 0
for d in range(k+1):
    for j in range(2**d):
        if s+j < n:
            print(tree[s+j], end = ' ')
    s += 2**d
    print()