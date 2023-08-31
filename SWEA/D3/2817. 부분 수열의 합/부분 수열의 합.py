# 부분 집합의 합을 구하는 함수
def subset(i, n, k, s):
    global cnt
    if i == n:
        if s == k:
            cnt += 1
            return
        return
    else:
        subset(i+1, n, k, s + arr[i])
        subset(i+1, n, k, s)

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    subset(0, n, k, 0)
    print(f'#{tc} {cnt}')
