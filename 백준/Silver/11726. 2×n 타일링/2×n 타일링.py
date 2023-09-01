import sys
input = sys.stdin.readline

# n이 1인 경우 1, 2인 경우 2
# n > 2 부터는 f(n) = f(n-1) + f(n-2)
def memo(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2: # n = 1인 경우를 고려
        dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = int(input().strip())

print(memo(n) % 10007)