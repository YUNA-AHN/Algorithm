n = int(input().strip())
cnt1 = cnt2 = 0
for _ in range(n):
    k = int(input().strip())
    if k == 1:
        cnt1 += 1
    else:
        cnt2 += 1

if cnt1 < cnt2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')