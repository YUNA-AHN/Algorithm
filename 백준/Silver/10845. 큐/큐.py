from collections import deque
import sys
input = sys.stdin.readline

def push(x):
    que.append(x)
    return

def pop():
    if len(que) == 0:
        print(-1)
    else:
        print(que.popleft())
    return

def size():
    print(len(que))
    return

def empty():
    if len(que):
        print(0)
    else:
        print(1)
    return

def front():
    if len(que):
        print(que[0])
    else:
        print(-1)
    return
def back():
    if len(que):
        print(que[-1])
    else:
        print(-1)
    return

command = {
    'push' : push,
    'pop' : pop,
    'size' : size,
    'empty' : empty,
    'front' : front,
    'back' : back
}

n = int(input().strip())
que = deque()
for i in range(n):
    com, *num = input().strip().split()
    if com == 'push':
        command[com](int(num[0]))
    else:
        command[com]()