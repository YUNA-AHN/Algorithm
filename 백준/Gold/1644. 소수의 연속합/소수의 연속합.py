import sys
import math
input = sys.stdin.readline

n = int(input().strip())

# 소수 구하는 알괴리즘
data = [True] * (n+1)
data[0] = False
data[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if data[i]:
        for j in range(i+i, n+1, i):
            data[j] = False

num_lst = []
for j in range(len(data)):
    if data[j]:
        num_lst.append(j)

# slow, fast
slow = fast = total = cnt = 0
while slow < len(num_lst) and slow <= fast:
    if total < n:
        total += num_lst[fast]
        fast += 1
    elif total > n:
        total = 0
        slow += 1
        fast = slow

    if total == n:
        cnt += 1
        slow += 1
        fast = slow
        total = 0
    else:
        if slow == len(num_lst) - 1 and fast >= len(num_lst):
            break
print(cnt)