import heapq
import sys
input = sys.stdin.readline

# 자연수 : 값 추가 / 0이면 가장 작은 값 출력하고 제거
n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, x)
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))