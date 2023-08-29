import sys
n = int(sys.stdin.readline())
weight = [int(sys.stdin.readline()) for _ in range(n)]

weight.sort()
len_weight = len(weight)
mx = 0
for i in range(n):
    mx = max(weight[i] * (len_weight - i), mx)

print(mx)