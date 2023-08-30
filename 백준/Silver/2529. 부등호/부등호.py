def perm(i, k):
    global arr, mx, mn
    if i == k:
        total = []
        # 부등호랑 조합 동시에 돌려야 한다.
        condition = True
        for j in range(len(arr)):
            if arr[j] == '>' and p[j] > p[j + 1]:
                pass
            elif arr[j] == '<' and p[j] < p[j + 1]:
                pass
            else:
                condition = False
                break
        if condition:
            total.append(''.join(map(str, p)))
    # print(total)

        for k in total:
            if int(mx) < int(k):
                mx = k
            if int(mn) > int(k):
                mn = k
        return

    else:
        for j in range(10):
            if used[j] == 0:
                used[j] = 1
                p[i] = j
                perm(i + 1, k)
                used[j] = 0

import sys

n = int(sys.stdin.readline())   # 부등호의 개수
arr = sys.stdin.readline().split() # 부등호
used = [0] * 10 # 0~9까지 사용 여부 체크
p = [0] * (n + 1) # 부등호 + 1 만큼 숫자 필요
perm_list = [] # 숫자 조합 받을 리스트 생성
mx = 0
mn = 100000000000

perm(0, n + 1)

print(mx)
print(mn)