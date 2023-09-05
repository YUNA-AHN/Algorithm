import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
for tc in range(T):
    command = input().strip() # 명령문
    n = int(input().strip()) # 배열 수
    arr = input().strip()[1:-1].split(',')

    que = deque(arr)
    flag = 0  # 뒤집기 횟수

    if n == 0:
        que = deque()

    for co in command:
        if co == 'R':
            flag += 1
        elif co == 'D':
            if len(que) == 0:
                print('error')
                break
            else:
                if flag % 2:
                    que.pop()
                else:
                    que.popleft()
    else:
        if flag % 2:
            que.reverse()
            print('[' + ','.join(que) + ']')
        else:
            print('[' + ','.join(que) + ']')