arr = [int(input()) for _ in range(9)]
mx = idx = 0
for i in range(len(arr)):
    if mx < arr[i]:
        mx = arr[i]
        idx = i
print(mx)
print(idx+1)
