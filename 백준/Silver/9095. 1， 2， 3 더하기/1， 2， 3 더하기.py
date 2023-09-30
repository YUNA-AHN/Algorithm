import sys
input = sys.stdin.readline

dp = [1] + [0] * 1001
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n + 1):
        dp[i] = dp[i-3] + dp[i -2] + dp[i - 1]

    print(dp[n])