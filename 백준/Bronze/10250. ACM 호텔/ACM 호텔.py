import sys
input = sys.stdin.readline

t = int(input().strip())
for tc in range(t):
    h, w, n = map(int, input().strip().split()) # 호텔 층수, 각 층의 방수, 몇번재 손님
    room = n // h
    floor = n % h
    
    if floor == 0:
        print((h*100) + room)
    else:
        print((floor*100) + room + 1)