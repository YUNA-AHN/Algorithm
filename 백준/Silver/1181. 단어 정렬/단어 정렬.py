import sys
n = int(sys.stdin.readline().strip())
my_dict = {}

for _ in range(n):
    text = sys.stdin.readline().strip()
    my_dict.setdefault(text, len(text))

my_dict = dict(sorted(my_dict.items(), key = lambda x: (x[1], x[0])))

for key in my_dict.keys():
    print(key)