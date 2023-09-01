def subset(i, n, s, k, times):
    global cnt
    # 깉이가 집합의 요소 수와 동일하다면
    # 집합의 합을 구하여 찾고자 하는 값과 동일한지 비교
    # 동일하다면 cnt + 1
    # 공집합인 경우를 제외하고자 times 변수 활용
    if i == n:
        if s == k and times > 0:
            cnt += 1
        return

    # 해당 원소가 포함되는 경우와 포함 되지 않는 경우
    subset(i+1, n, s + arr[i], k, times + 1)
    subset(i+1, n, s, k, times)


import sys
input = sys.stdin.readline

n, s = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
cnt = 0
subset(0, n, 0, s, 0)
print(cnt)