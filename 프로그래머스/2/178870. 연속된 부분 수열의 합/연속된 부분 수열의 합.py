def solution(sequence, k):
    answer = []
    start, end = 0, 0
    first, second = 1000000, 2000000
    total = sequence[0]
    sequence += [0]
    
    while end < len(sequence) - 1:
        # 총합이 k보다 작거나 같은 경우
        if total <= k:
            # k와 같은 경우 & 더 짧은지 비교, 갱신
            if total == k and end - start < second - first:
                first, second = start, end
            # 마지막 칸 더해주기
            end += 1
            total += sequence[end]
        else:
            # start 갱신해주기
            start += 1
            total -= sequence[start - 1]
    
    return [first, second]