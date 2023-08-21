def bfs(a, b):
    global visited
    que = []
    que.append([a, 0])
    while que:
        val, cnt = que.pop(0)
        if val == b: # 목표 값에 도달하면 멈추기
            break
        if val * 2 <= b or val * 10 + 1 <= b: # 둘 중에 하나에 걸리면 들어오세요
            if val * 2 <= b:
                que.append([val * 2, cnt + 1])
                visited.append([val * 2, cnt + 1])

            if val * 10 + 1 <= b:
                que.append([val * 10 + 1, cnt + 1])
                visited.append([val * 10 + 1, cnt + 1])



a, b = map(int, input().split())
visited = []
bfs(a, b)

ans = -1
for i in range(len(visited)):
    if visited[i][0] == b and visited[i][1] > 0:
        ans = visited[i][1] + 1
        break
    else:
        ans = -1

print(ans)
