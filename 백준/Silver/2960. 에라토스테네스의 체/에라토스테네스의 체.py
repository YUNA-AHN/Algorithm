import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = list(range(2, n+1))

cnt = 0
while arr:
    perm = arr[0]
    for num in arr:
        if num % perm == 0:
            cnt += 1
            if cnt == m:
                print(num)
                break
            arr.remove(num)
