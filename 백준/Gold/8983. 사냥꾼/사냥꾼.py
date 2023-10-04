'''
사냥꾼
거리 : abs(x-a) + b
- 일단 동물의 x좌표와 y좌표 자체적으로 사정거리 이내인지 체크
- 이후에 거리 계산하여 사냥 가능 동물 수 체크
- 동물을 돌리자 !

4 8 4
6 1 4 9
7 2
3 3
4 5
5 1
2 2
1 4
8 4
9 4


// 5
1 5 3
3
2 2
1 1
5 1
4 2
3 3
'''
import sys
input = sys.stdin.readline

def binary(left, right, x, y):
    '''
    중앙값이 사정거리에 포함된다면 +1
    사정거리로 보면 될듯...!
    abs(x-a) + b
    '''
    global res
    if right < left:
        return
    mid = (left + right) // 2
    if abs(arr[mid] - x) <= l - y:
        res += 1
    elif arr[mid] > x:
        binary(0, mid-1, x, y)
    else:
        binary(mid+1, right, x, y)

# 사대의 수, 동물의 수, 사정 거리
m, n, l = map(int, input().strip().split())
arr = list(map(int, input().strip().split())) # 사대의 좌표
arr.sort()
res = 0 # 사냥한 동물의 수

for _ in range(n):
    x, y = map(int, input().strip().split())

    # y가 사정거리 이상이라면 넘기기
    if y > l:
        continue
    # 이분 탐색
    left = 0
    right = m - 1
    binary(left, right, x, y)
print(res)