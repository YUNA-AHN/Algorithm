from collections import deque
import sys
input = sys.stdin.readline

def push_front(x):
    que.appendleft(x)
    return

def push_back(x):
    que.append(x)
    return

def pop_front():
    if len(que) == 0:
        print(-1)
    else:
        print(que.popleft())
    return

def pop_back():
    if len(que) == 0:
        print(-1)
    else:
        print(que.pop())
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
    'push_front' : push_front,
    'push_back' : push_back,
    'pop_front' : pop_front,
    'pop_back' : pop_back,
    'size' : size,
    'empty' : empty,
    'front' : front,
    'back' : back
}

n = int(input().strip())
que = deque()
for i in range(n):
    com, *num = input().strip().split()
    if com == 'push_front' or com == 'push_back' :
        command[com](int(num[0]))
    else:
        command[com]()