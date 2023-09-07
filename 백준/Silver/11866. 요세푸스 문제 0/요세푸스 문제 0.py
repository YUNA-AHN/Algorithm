
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

# 출력을 위하여 문자열 리스트로 생성
que = deque(map(str, list(range(1, n+1))))

res = []
cnt = 1
while que:
    # k번째가 아니라면 pop하여 맨 뒤로
    if cnt % k:
        que.append(que.popleft())
        cnt += 1
    # k번째라면 결과 리스트에 입력, cnt 초기화
    else:
        res.append(que.popleft())
        cnt = 1

print('<' + ', '.join(res) + '>')