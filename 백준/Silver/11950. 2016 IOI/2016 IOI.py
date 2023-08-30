import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(n)]

mn = 10000000
for i in range(1, n-1):
    for j in range(i+1, n):
        sum_v = 0
        for l in range(n):
            if l < i:
                sum_v += m - arr[l].count('W')
            elif l < j:
                sum_v += m - arr[l].count('B')
            else:
                sum_v += m - arr[l].count('R')
        mn = min(mn, sum_v)
print(mn)