import sys
t = int(sys.stdin.readline().strip())
for tc in range(1, t+1):
    r, s = sys.stdin.readline().split()

    ans = ''
    for i in range(len(s)):
        ans += s[i] * int(r)

    print(ans)