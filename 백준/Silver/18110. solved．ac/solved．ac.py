import sys
input = sys.stdin.readline

n = int(input().strip()) # 의견의 개수
arr = [int(input().strip()) for _ in range(n)] # 의견
arr.sort()

if n == 0:
    print(0)
else:
    # 상하위 15%를 확인하기 위하여
    # 0.0000001 더해주는 이유 : 파이썬에서 0.5 초과가 기준이기 때문
    k = round(n * 0.15 + 0.0000001)
    avg = round(sum(arr[k:n-k])/(n-k*2) + 0.0000001)

    print(avg)
