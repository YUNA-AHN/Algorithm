import sys
import math
input = sys.stdin.readline

def is_primenum(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


n, m = map(int, input().strip().split())

# 소수 판정하기
for i in range(n, m+1):
    if is_primenum(i):
        print(i)