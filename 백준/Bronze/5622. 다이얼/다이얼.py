import sys
s = sys.stdin.readline().strip()
sv = 0
for i in s:
    if i in 'ABC':
        sv += 3
    elif i in 'DEF':
        sv += 4
    elif i in 'GHI':
        sv += 5
    elif i in 'JKL':
        sv += 6
    elif i in 'MNO':
        sv += 7
    elif i in 'PQRS':
        sv += 8
    elif i in 'TUV':
        sv += 9
    else:
        sv += 10
print(sv)