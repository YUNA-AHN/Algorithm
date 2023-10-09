from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs(comb):
    visited = set([comb[0]])
    que = deque()
    que.append(comb[0])
    total = 0 # 해당 구역의 사람을 카운트
    while que:
        node = que.popleft()
        total += people[node]
        for nxt in graph[node]:
            if nxt not in visited and nxt in comb:
                que.append(nxt)
                visited.add(nxt)
    return total, len(visited)

# 선거구 개수
n = int(input().strip())

# 구역별 인구수
people = [0] + list(map(int, input().strip().split()))

# 인접리스트 graph 생성
graph = [[0]]
for i in range(n):
    region, *node = map(int, input().strip().split())
    graph.append(node)


# 결과를 받을 result 생성
result = sys.maxsize

# 조합 : 적어도 하나는 존재해야 하므로 1부터 n//2까지
for i in range(1, n//2 + 1):
    combs = list(combinations(range(1, n + 1), i))
    # 생성해준 순열을 하나씩 돌면서
    for comb in combs:
        total_a, cnt_1 = bfs(comb)
        total_b, cnt_2 = bfs([i for i in range(1, n+1) if i not in comb])

        # 두 선거구의 모든 노드가 연결되어 있느닞 확인
        if cnt_1 + cnt_2 == n:
            result = min(result, abs(total_a - total_b))

if result == sys.maxsize:
    print(-1)
else:
    print(result)
