from collections import deque
import sys
input = sys.stdin.readline

def push(x):
    stack.append(x)
    return

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())
    return

def size():
    print(len(stack))
    return

def empty():
    if len(stack):
        print(0)
    else:
        print(1)
    return

def top():
    if len(stack):
        print(stack[-1])
    else:
        print(-1)
    return

command = {
    'push' : push,
    'pop' : pop,
    'size' : size,
    'empty' : empty,
    'top' : top
}

n = int(input().strip())
stack = deque()
for i in range(n):
    com, *num = input().strip().split()
    if com == 'push':
        command[com](int(num[0]))
    else:
        command[com]()