import sys
input = sys.stdin.readline

# n이 0, 1인 경우 1
# n > 1 부터는 f(n) = f(n-1) + f(n-2) * 2
def memo(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    return dp[n]
while True:
    try:
        n = int(input().strip())
        k = memo(n)
        print(k)
    except:
        break
