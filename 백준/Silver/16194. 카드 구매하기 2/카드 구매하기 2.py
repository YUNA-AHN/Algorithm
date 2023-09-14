import sys
input = sys.stdin.readline

# dp[i] = 카드 i개 구매하는 최소 가격
# p[k] = k개가 들어있는 카드팩 가격 이라고 했을때
n = int(input().strip())
arr = [0] + list(map(int, input().strip().split()))
# 시작을 0으로 잡고, 나머지는
dp = [0] + [10 ** 7] * (n)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], arr[j] + dp[i-j])

print(dp[n])
