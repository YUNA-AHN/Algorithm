import sys
input = sys.stdin.readline


def find(x):
    # 자기 자신이 부모라면 자기 자신 출력
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    # 아니라면 그 부모를 또 찾아보시지요
    return parents[x]

# 더 작은 값으로 합쳐줍니당
def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        if px > py:
            parents[px] = py
        else:
            parents[py] = px

# 노드의 개수와 edges의 개수
n, m = map(int, input().strip().split())

# 시작점과 도착점
start, end = map(int, input().strip().split())

# 리스트 생성
graph = []
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    graph.append((u, v, w))

# 가중치 기준으로 내림차순 정렬
graph.sort(key = lambda x: x[2], reverse=True)

parents = [i for i in range(n)]
mn = 10000

for i in range(m):
    # 시작점과 도착점이 동일해진다면! 연결된거니까 멈춘다
    if find(start) == find(end):
        break
    x, y, w = graph[i]
    # 부모가 다르다면 연결해주세욥
    if find(x) != find(y):
        union(x, y)
        if mn > w:
            mn = w

print(mn)