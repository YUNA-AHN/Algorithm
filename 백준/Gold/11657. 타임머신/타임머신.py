import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
# 간선 정보 입력
edges = []
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    edges.append((u, v, w))

inf = sys.maxsize # 매우 큰 값 생성
def bellman_ford(start):
    # 노드 번호사 1번부터 시작하므로 n+1
    dist = [inf] * (n+1)
    # 시작노드 = 0
    dist[start] = 0

    # n-1번 순회
    for _ in range(n-1):
        for u, v, w in edges:
            new_cost = dist[u] + w
            # 새로 계산된 값이 기존의 최소비용보다 작다면 갱신
            # dist[u]가 계속 inf이면 이전에 방문한 적이 없다는 것이기 때문...
            if dist[v] > new_cost and dist[u] != inf:
                dist[v] = new_cost

    # 음수 사이클 확인하기 위하여 한 번 더 돌리기
    minus_cycle = False
    for u, v, w in edges:
        if dist[u] != inf and dist[v] > dist[u] + w:
            minus_cycle = True

    return minus_cycle, dist

minus_cycle, short_dist = bellman_ford(1)

if not minus_cycle:
    for i in range(2, n+1):
        if short_dist[i] != inf:
            print(short_dist[i])
        else:
            print(-1)
else:
    print(-1)