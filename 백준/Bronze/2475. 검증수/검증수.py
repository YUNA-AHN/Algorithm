import sys
input = sys.stdin.readline

arr = list(map(int, input().strip().split()))

print(sum(map(lambda x: x ** 2, arr)) % 10)