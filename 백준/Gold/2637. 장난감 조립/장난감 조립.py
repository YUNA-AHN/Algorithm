from collections import deque
import sys
input = sys.stdin.readline


# n : 3이상 100 이하, 1부터 n-1은 기본 부품과 중간 부품
# n 은 완제품
# 필요한 기본 부품의 수 한줄에 하나씩 출력, 번호가 작은 것부터
n = int(input().strip())
m = int(input().strip()) # edges

graph = [[] for _ in range(n+1)]
in_deep = [0] * (n+1)

for _ in range(m):
    a, b, w = map(int, input().strip().split())
    # b - a로 진행!
    graph[b].append((a, w)) # a를 만드는데 b가 c개 필요하다!
    in_deep[a] += 1

# 각 부푼 번호 별 필요한 부품의 개수
needs = [[0] * (n+1) for _ in range(n+1)]

#  위상정렬
que = deque()
for idx in range(1, n+1):
    # 진입 차수가 0이면 기본 인자임!
    if in_deep[idx] == 0:
        que.append(idx)

while que:
    now = que.popleft()
    # now로 만들 수 있는 부품 번호, 필요한 now의 개수
    for nxt, val in graph[now]:
        # 지금 인자가 기본 키라면, 중간 부품이 필요한 값 입력해줌
        if needs[now].count(0) == n + 1:
            needs[nxt][now] += val
        else:
            # 중간 부품이라면,
            for i in range(1, n+1):
                needs[nxt][i] += needs[now][i] * val

        in_deep[nxt] -= 1
        if in_deep[nxt] == 0:
            que.append(nxt)

for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)