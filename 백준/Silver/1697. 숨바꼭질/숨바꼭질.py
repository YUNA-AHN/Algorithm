from collections import deque
def bfs(n, k, cnt):
    que = deque([[n, cnt]])
    while que:
        n, cnt = que.popleft()
        if n == k:
            return cnt

        cnt += 1
        if 0 <= n+1 <= 100000 and n <= k and visited[n + 1] == 0:
            que.append([n + 1, cnt])
            visited[n + 1] = 1
        if 0 <= n*2 <= 100000 and n <= k and visited[n * 2] == 0:
            que.append([n * 2, cnt])
            visited[n * 2] = 1
        if 0 <= n-1 <= 100000 and visited[n - 1] == 0:
            que.append([n - 1, cnt])
            visited[n - 1] = 1

n, k = map(int, input().split())

visited = [0] * 100001
print(bfs(n, k, 0))
