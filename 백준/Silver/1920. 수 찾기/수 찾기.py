def binary(k, n_list, start, end):
    if start > end:
        return 0
    
    middle = (start + end) // 2
    if n_list[middle] == k:
        return 1
    elif n_list[middle] < k:
        return binary(k, n_list, middle+1, end)
    else:
        return binary(k, n_list, start, middle - 1)

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = sorted(list(map(int, input().strip().split())))

# 해당 카드가 존재하는지?
m = int(input().strip())
card = list(map(int, input().strip().split()))

for num in card:
    print(binary(num, arr, 0, n-1))