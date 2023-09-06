import sys
input = sys.stdin.readline

arr = list(map(int, input().strip().split()))

if arr == sorted(arr):
    print('ascending')
elif arr == sorted(arr, reverse=True):
    print('descending')
else:
    print('mixed')