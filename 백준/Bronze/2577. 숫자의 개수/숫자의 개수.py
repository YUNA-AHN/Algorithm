import sys
input = sys.stdin.readline

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

res = a * b * c

for i in range(10):
    print(str(res).count(str(i)))
