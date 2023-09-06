import sys
input = sys.stdin.readline

t = int(input().strip())
for tc in range(t):
    arr = input().strip()

    cnt = total = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)