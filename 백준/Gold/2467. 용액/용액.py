import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

arr.sort()

start = 0
end =  len(arr)-1

res = sys.maxsize
# start가 end보다 작은 값인 동안에
while start < end:
    # res 값보다 작다면, rs, re, res 갱신
    if abs(arr[start] + arr[end]) < res:
        rs, re = start, end
        res = abs(arr[start] + arr[end])

    if abs(arr[start+1] + arr[end]) > abs(arr[start] + arr[end-1]):
        end -= 1
    else:
        start += 1

print(arr[rs], arr[re])