from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
res = [0] * n
stack = deque()

for i in range(n):
    # top보다 작거나 같은 경우에만 stack에 입력
    if not stack:
        stack.append(i)
    elif arr[stack[-1]] >= arr[i]:
        stack.append(i)
    else:
        # stack이 존재하는 동안
        # top보다 큰 경우 자기보다 작을 때까지 pop
        while stack:
            # top이 new보다 작거나 같다면 pop
            if arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                res[idx] = arr[i]
            # top이 더 크다면 break
            else:
                break
        stack.append(i)
        # 뽑히는 애들 값을 arr[i]로 입력

for i in res:
    if i == 0:
        print(-1, end=" ")
    else:
        print(i, end=" ")
print()