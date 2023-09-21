import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        cnt[px] += cnt[py]
        parents[py] = px

    return cnt[px]


t = int(input().strip())
for _ in range(t):
    parents = dict()
    cnt = dict()
    n = int(input().strip())
    for _ in range(n):
        a, b = input().split()
        # 친구 이름이 존재하지 않는다면, 키를 추가해주고 값으로 친구 이름을 입력
        parents.setdefault(a, a)
        parents.setdefault(b, b)
        # 카운트 딕셔너리. 존재하지 않는다면 키를 추가해주고 1 입력
        cnt.setdefault(a, 1)
        cnt.setdefault(b, 1)

        res = union(a, b)
        print(res)