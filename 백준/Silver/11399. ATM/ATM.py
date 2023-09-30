import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()

total = 0
for i in range(n):
    for j in range(i+1):
        total += arr[j]

print(total)