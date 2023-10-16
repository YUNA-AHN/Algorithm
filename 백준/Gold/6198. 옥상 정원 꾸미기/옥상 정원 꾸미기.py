import sys
input = sys.stdin.readline

n = int(input().strip())
arr = []

cnt = 0
for _ in range(n):
    h = int(input().strip())
    if len(arr) == 0:
        arr.append(h)
        cnt += len(arr)-1
    else:
        # top이 더 크다면, append
        if arr[-1] > h:
            arr.append(h)
            cnt += len(arr)-1
        else:
            # top이 더 작다면
            # h가 top보다 작을때까지 pop
            while arr:
                arr.pop()
                if arr and arr[-1] > h:
                    arr.append(h)
                    cnt += len(arr)-1
                    break
            if not arr:
                arr.append(h)
                cnt += len(arr)-1

print(cnt)
