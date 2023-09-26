import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip()) # 회원의 수
graph = [[] for _ in range(n+1)]
while True:
    # 두 회원이 친구이다!
    u, v = map(int, input().strip().split())

    # -1, -1이면 입력 종료
    if u == v == -1:
        break
    # 왕복 더 해주기
    graph[u].append(v)
    graph[v].append(u)

check = [51] + [0] * (n)
# 모든 노드를 시작점으로
for i in range(1, n+1):
    cnt = 1
    visited = [0] * (n+1)
    que = deque()
    que.append(i)
    visited[i] = 1
    while que:
        node = que.popleft()
        # 노드에서 갈 수 있는 만큼 돌면서
        for j in graph[node]:
            if visited[j] == 0:
                visited[j] += visited[node] + 1
                que.append(j)
                cnt += 1
    if cnt == n:
        check[i] = max(visited)

mn = min(check)-1
res = []
for idx in range(1, n+1):
    if check[idx]-1 == mn:
        res.append(idx)

print(mn, len(res))
print(*sorted(res))