import sys
input = sys.stdin.readline

text = input().strip().upper()
num = dict()

for char in text:
    num.setdefault(char,0)
    num[char] += 1

mx = max(num.values())

cnt = 0
ans = ''
for key, value in num.items():
    if value == mx:
        cnt += 1
        ans = key

if cnt >= 2:
    print('?')
else:
    print(ans)