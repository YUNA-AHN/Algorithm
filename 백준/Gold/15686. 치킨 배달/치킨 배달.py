from collections import deque
import sys
input = sys.stdin.readline

# 치킨 거리 : 집과 가장 가짜운 치킨집 사이의 거리
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# 0 빈칸, 1은 집, 2는 치킨집
# 가장 작은 도시의 치킨 거리! 폐업 x 치킨  M
# 가장 치킨거리가 작게되는 가게 빼고 다 폐업
# 폐업하는 부분집합..? 필요한가...?
# 돌다가 최소 거리보다 커지면 가지치기 필요

# 폐업안 할 치킨집 조합 고르기
# nCr : n개에서 r개를 뽑는 조합 함수
# n = 모든 치킨집 수, r은 뽑을 치킨집의 수, s는 시작할 인덱스
def ncr(n, r, idx):
    # 기저조건 : m개를 모두 뽑은 경우
    if r == 0:
        chi.append(deque(s))
        return
    for k in range(idx, n - r + 1):
        s[r-1] = sub[k]
        ncr(n, r - 1, k + 1)


# bfs로 정리
# 인덱스 여러개로 받지 말기
# chi 받아서 돌고 1이상 되면 더하기
def bfs(que):
    global total
    while que:
        i, j = que.popleft()
        for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and (ni, nj) not in check:
                que.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                # 만약 집이라면 total에 더해주기
                if arr[ni][nj] == 1:
                    total += visited[ni][nj]

                if total > mn:
                    return


n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

# 치킨집 위치 찾기
sub = deque() # 치킨집 위치 좌표 리스트
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            sub.append((i,j))

# 부분 집합 받을 리스트 생성
s = [0] * m
# 치킨집 개수
c_len = len(sub)
# 치킨집 위치 좌표 받기
chi = deque()
ncr(c_len, m, 0)

# 치킵집 수와 폐업 안시킬 가게 수 같으면 subset 필요 업지 않나?
mn = 10 ** 7
for que in chi:
    visited = [[0] * n for _ in range(n)] # 방문 체크열
    check = que.copy()
    total = 0 # 치킨 거리
    bfs(que)
    mn = min(mn, total)

print(mn)
