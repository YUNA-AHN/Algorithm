# 수 묶기
import sys
input  = sys.stdin.readline

n =  int(input().strip())

total = cnt = 0
arr_big = []
arr_small = []

for _ in range(n):
    num = int(input().strip())
    
    if num >= 2:
        arr_big.append(num)
    elif num == 1:
        total += 1
    elif num == 0:
        cnt += 1
    else:
        arr_small.append(num)
        
arr_big.sort()
arr_small.sort()

while len(arr_small) > 1:
    a = arr_small.pop(0)
    b = arr_small.pop(0)
    total += a*b
    
arr_small = arr_small[cnt:]

if arr_small:
    total += arr_small[0]


while len(arr_big) > 1:
    a = arr_big.pop()
    b = arr_big.pop()
    total += a*b
    
if arr_big:
    total += arr_big[0]

print(total)