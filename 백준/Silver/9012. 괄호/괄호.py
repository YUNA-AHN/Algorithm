from collections import deque
import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    arr = list(input().strip())

    condition = True

    stack = deque()
    for item in arr:
        if item == '(':
            stack.append(item)
        else:
            # 스택이 비었는데 닫힌 괄호가 들어오는 경우 : 닫는 괄호가 더 많은 경우
            if len(stack) == 0:
                condition = False
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    condition = False
                    break

    if stack or condition == False:
        print('NO')
    else:
        print('YES')