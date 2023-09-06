from collections import deque
import sys
input = sys.stdin.readline

k = int(input().strip())
stack = deque()

for _ in range(k):
    num = int(input().strip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))