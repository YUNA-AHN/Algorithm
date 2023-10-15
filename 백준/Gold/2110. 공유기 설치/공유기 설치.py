import sys
input = sys.stdin.readline

def binary(arr, start, end):
    global ans
    while start < end:
        mid = (start+end)//2
        cnt = 1
        check = arr[0]
        for k in range(n):
            if arr[k] - check >= mid:
                cnt += 1
                check = arr[k]
        if cnt >= c:
            ans = mid
            start = mid + 1
        elif cnt < c:
            end = mid

n, c = map(int, input().strip().split())

arr = []
for i in range(n):
    t = int(input())
    arr.append(t)
arr.sort()

ans = 0

# 공유기가 2대 뿐이라면
# 두 공유기가 가장 멀도록 설치해야 하므로 양 끝에 설치
if c == 2:
    print(arr[-1]-arr[0])
else:
    binary(arr, 1, arr[-1]-arr[0])
    print(ans)