def tree(u):
    '''
    cnt : 방문한 국가 수
    - 이미 방문한 적이 있다면 카운팅 x
    - 방분한 국가 수가 n과 동일해지면 종료
    '''
    global cnt, mn
    if cnt == n:
        return
    for i in arr[u]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = 1
            tree(i)

import sys
input = sys.stdin.readline

t = int(input().strip())
for tc in range(t):
    n, m = map(int, input().strip().split())
    # 각 노드에서 방문할 수 있는 방문 리스트 생성
    arr = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        u, v = map(int, input().strip().split())
        arr[u].append(v)
        arr[v].append(u)

    cnt = 0
    mn = 10 ** 7
    tree(1)
    print(cnt-1)
