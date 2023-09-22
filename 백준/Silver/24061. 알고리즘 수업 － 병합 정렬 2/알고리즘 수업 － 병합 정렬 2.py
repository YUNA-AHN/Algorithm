# 알고리즘 수업 - 병합 정렬
import sys
input = sys.stdin.readline

def merge_sort(arr, k):
    def divide(left, right):
        global cnt
        nonlocal arr
        # 쪼갤 것이 2개 이상 남이있을 떄까지
        if right - left < 2:
            return
        mid = (left + right) // 2 + ((right - left) % 2)
        divide(left, mid)
        divide(mid, right)
        if cnt == k:
            return
        merge(left, mid, right)

    def merge(left, mid, right):
        nonlocal arr, k
        global cnt
        i, j = left, mid
        t = 0
        merged_arr = []
        while i < mid and j < right:
            if arr[i] < arr[j]:
                merged_arr.append(arr[i])
                i += 1
            else:
                merged_arr.append(arr[j])
                j += 1
        while i < mid:
            merged_arr.append(arr[i])
            i += 1
        while j < right:
            merged_arr.append(arr[j])
            j += 1

        i = left
        idx = 0
        while i < right:
            arr[i] = merged_arr[idx]
            i += 1
            idx += 1
            cnt += 1

            if cnt == k:
                return


    left = 0
    right = len(arr)
    return divide(left, right)

n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
cnt = 0
merge_sort(arr, k)

if cnt == k:
    print(*arr)
else:
    print(-1)