# 거짓말
# 거짓말쟁이로 알려지지 않으면서 과장된 이야기 가능한 파티의 개수
import sys

input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union_truth(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return
    # 더 작은 값으로 유니온
    if px < py:
        parents[py] = px
    else:
        parents[px] = py


def union(x, y):
    px = find(x)
    py = find(y)

    # 부모 노드가 다를 때
    if px != py:
        if truth:
            # px의 부모가 진실을 아는 사람이라면 px로
            if px == min(arr_t):
                parents[py] = px
            # py의 부모가 진실을 아는 사람이라면 py로
            elif py == min(arr_t):
                parents[px] = py
            # 암것도 아니라면 일단 작은 수로
            else:
                if px < py:
                    parents[py] = px
                else:
                    parents[px] = py
        else:
            if px < py:
                parents[py] = px
            else:
                parents[px] = py

# 사람의 수, 파티의 수
n, m = map(int, input().strip().split())

# 자기 자신으로 초기화 !
parents = [i for i in range(n + 1)]

# 진실을 아는 사람의 수, 번호
truth, *arr_t = map(int, input().strip().split())

# 진실을 아는 사람끼리 미리 묶기 : 최솟값으로
if truth >= 2:
    for idx in range(truth-1):
        union_truth(arr_t[idx], arr_t[idx + 1])

# 파티의 수 만큼 순회
# 진실을 아는 사람이 있거나 같이 파티에 참석한 적이 있다면(조상노드가 같다면...) 그 파티는 못감
arr = [list(map(int, input().strip().split())) for _ in range(m)]

# 일단 파티에에서만 사람들은 다 엮어주어야 함
# 사람 숫자만큼 순회하면서 unione 해주기
for i in range(m):
    people, *arr_p = arr[i]
    if people >= 2:
        for idx in range(people-1):
            # 파티에 온 사람 다 union
            union(arr_p[idx], arr_p[idx+1])
cnt = 0
for i in range(m):
    people, *arr_p = arr[i]
    condition = True
    for person in arr_p:
        if find(person) in arr_t:
            condition = False
    if condition:
        cnt += 1
print(cnt)