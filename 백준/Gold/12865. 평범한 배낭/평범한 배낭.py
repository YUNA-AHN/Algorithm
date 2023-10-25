'''
평범한 배낭 점화식
dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi] + vi)
n개를 가지고 weight가 w일 때 값은
n-1개에서 n번째 물픔을 넣지 않았을 때와, 넣었을 때를 비교하여 더 큰 값 입력
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = []

for _ in range(n):
    # 무게와 가중치
    w, v = map(int, input().strip().split())
    arr.append((w, v))

# 선택할 수 있는 개수 (n+1)개 X 담을 수 있는 Weight (0~k)
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1,k+1):
        if 0 <= j - arr[i-1][0] <= k:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - arr[i-1][0]] + arr[i-1][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
