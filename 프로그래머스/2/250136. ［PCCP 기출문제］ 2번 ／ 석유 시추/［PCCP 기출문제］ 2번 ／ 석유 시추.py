def solution(land):
    from pprint import pprint
    from collections import deque
    answer = 0
    dump =  10
    oil = 0
    oil_lst = []
    r, c = len(land), len(land[0])
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1 and visited[i][j] == 0:
                que = deque()
                que.append((i, j))
                land[i][j] = dump
                visited[i][j] = 1
                oil += 1
                while que:
                    x, y = que.popleft()
                    for a, b in [[0,1], [0,-1], [-1,0], [1,0]]:
                        nx, ny = x + a, y + b
                        if 0 <= nx < r and 0 <= ny < c and land[nx][ny] == 1 and visited[nx][ny] == 0:
                            que.append((nx, ny))
                            visited[nx][ny] = 1
                            oil += 1
                            land[nx][ny] = dump
                dump += 1
                oil_lst.append(oil)
                oil = 0
    for col in zip(*land):
        total = 0
        for idx in list(set(col)):
            if idx != 0:
                total += oil_lst[idx-10]
        answer = max(total, answer)
    return answer