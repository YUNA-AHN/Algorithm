import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
password = dict()

for _ in range(n):
    site, pw = input().strip().split()
    password.setdefault(site,'')
    password[site] = pw

for _ in range(m):
    res = input().strip()
    print(password[res])