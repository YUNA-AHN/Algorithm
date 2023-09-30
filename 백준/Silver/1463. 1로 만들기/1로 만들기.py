from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# n+1 까지의 방문체크열 생성
visited = [0] * (n+1)

que = deque()
que.append(n)
num = n
while num != 1:
    num = que.popleft()
    if num % 3 == 0 and visited[num // 3] == 0:
        k = num // 3
        que.append(k)
        visited[num // 3] = visited[num] + 1
    if num % 2 == 0 and visited[num // 2] == 0:
        k = num // 2
        que.append(k)
        visited[num // 2] = visited[num] + 1
    if num > 1 and visited[num - 1] == 0:
        k = num - 1
        que.append(k)
        visited[num - 1] = visited[num] + 1

print(visited[1])