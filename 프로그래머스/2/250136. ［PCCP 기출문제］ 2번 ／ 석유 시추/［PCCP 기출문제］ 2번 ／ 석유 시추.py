def solution(land):
    from pprint import pprint
    from collections import deque
    answer = 0
    dump =  10 # 석유 덩어리 번호
    oil = 0 # 석유 양
    oil_lst = [] # 석유 양 리스트
    r, c = len(land), len(land[0])
    visited = [[0] * c for _ in range(r)]
    # 순회하면서 1인 경우 bfs 진행
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1 and visited[i][j] == 0:
                que = deque()
                que.append((i, j))
                land[i][j] = dump
                visited[i][j] = 1
                oil += 1 # 석유 양 더하기
                while que:
                    x, y = que.popleft()
                    for a, b in [[0,1], [0,-1], [-1,0], [1,0]]:
                        nx, ny = x + a, y + b
                        if 0 <= nx < r and 0 <= ny < c and land[nx][ny] == 1 and visited[nx][ny] == 0:
                            que.append((nx, ny))
                            visited[nx][ny] = 1
                            oil += 1
                            land[nx][ny] = dump
                dump += 1 # 인덱스 번호 + 1
                oil_lst.append(oil) # 석유 양 리스트
                oil = 0 # 석유 양 초기화
    # 열 별로 set 하여 양 더하기
    for col in zip(*land):
        total = 0
        for idx in list(set(col)):
            if idx != 0:
                total += oil_lst[idx-10]
        # 석유 양이 가장 많은 경우
        answer = max(total, answer)
    return answer