from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 숫자로 이루어진 새로운 맵 생성
    si, sj, ei, ej, li, lj = 0, 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                si, sj = i, j
            elif maps[i][j] == "E":
                ei, ej = i, j
            elif maps[i][j] == "L":
                li, lj = i, j
    
    def bfs(si, sj, ei, ej):
        visited = [[0] * m for _ in range(n)]
        que = deque()
        que.append((si, sj))

        while que:
            x, y = que.popleft()

            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
        return visited[ei][ej]


    dist1 = bfs(si, sj, li, lj)
    dist2 = bfs(li, lj, ei, ej)

    
    print(dist1, dist2)
    answer = 0
    if dist1 and dist2:
        answer = dist1 + dist2
    else:
        answer = -1
        
    return answer