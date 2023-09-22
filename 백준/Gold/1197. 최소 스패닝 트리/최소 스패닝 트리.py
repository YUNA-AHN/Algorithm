# prim : 임의의 정점 선택, 인접한 정점 중 최소 비용 like bfs : 모든 노드 방문시 중단
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().strip().split())
# 인접 리스트 생성
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def prim(graph, start):
    visited = [False] * (V+1) # 방문 체크열
    min_heap = [(0, start)] # 첫 시작 정점의 가중치는 0
    MST = []

    while min_heap:
        cost, node = heapq.heappop(min_heap) # 가중치 제일 적은 정점 pop
        if visited[node]: # 방문한 적 있다면 skip
            continue
        # 방문한 적 없다면, 방문 체크 후 MST에 입력
        visited[node] = True
        MST.append((node, cost))

        for nxt, cost in graph[node]:
            # 방문한 적이 없다면, 우선 순위 큐에 입력
            if not visited[nxt]:
                heapq.heappush(min_heap, (cost, nxt))
    return MST

# 노드 번호가 1부처 시작하기 때문에 1부터 시작 !
MST = prim(graph, 1)

total = 0
for node, cost in MST:
    total += cost
    
print(total)
