arr = [list(map(int, input().split())) for _ in range(9)]
mx = ri = rj =0
for i in range(9):
    for j in range(9):
        if arr[i][j] > mx:
            mx = arr[i][j]
            ri, rj = i, j

print(mx)
print(ri + 1, rj + 1)