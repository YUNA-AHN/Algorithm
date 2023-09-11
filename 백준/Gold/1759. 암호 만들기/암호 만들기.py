# 암호만들기
# 조합함수 작성
def ncr(n, r, s):
    # 더 이상 뽑지 않아도 된다면  tr과 nes_s를 더하고 정렬한 후 append
    if r == 0:
        res.append(''.join(sorted(tr + new_s)))
        return
    else:
        for i in range(s, n - r + 1):
            # 이전에 추가되지 않은 값일때만
            if visited[i] == 0:
                new_s[r-1] = arr[i]
                ncr(n, r-1, i + 1)
                
import sys
input = sys.stdin.readline

l, c = map(int, input().strip().split())
arr = list(input().strip().split())
mo = []
ja = []
visited = [0] * c
res = []


# mo와 ja에 각각 모음, 자음에 해당하는 인덱스 입력
for i in range(len(arr)):
    if ord(arr[i]) in [97, 101, 105, 111, 117]:
        mo.append(i)
    else:
        ja.append(i)


for i in mo:
    for j in range(len(ja)-1):
        for k in range(j+1, len(ja)):
            # 암호를 받을 new_s 생성
            new_s = [0] * (l-3)

            tr = [0] * 3
            visited[i] = 1
            visited[ja[j]] = 1
            visited[ja[k]] = 1
            tr[0] = arr[i]
            tr[1] = arr[ja[j]]
            tr[2] = arr[ja[k]]
            ncr(c, l-3, 0)
            visited[i] = 0
            visited[ja[j]] = 0
            visited[ja[k]] = 0

for item in sorted(list(set(res))):
    print(item)
    
# print(sorted(list(set(res))))