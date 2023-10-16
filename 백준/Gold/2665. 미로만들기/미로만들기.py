import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    que = [(0, 0, 0)] # w, i, j
    inf = sys.maxsize
    # 최댓값
    dist = [[inf] * n for _ in range(n)]
    dist[0][0] = 0

    while que:
        w, i, j = heapq.heappop(que)
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 1:
                    new_cost = w
                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        heapq.heappush(que, (new_cost, ni, nj))
                else:
                    new_cost = w + 1
                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        heapq.heappush(que, (new_cost, ni, nj))
    return dist[n-1][n-1]


n = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(n)]

ans = dijkstra()
print(ans)