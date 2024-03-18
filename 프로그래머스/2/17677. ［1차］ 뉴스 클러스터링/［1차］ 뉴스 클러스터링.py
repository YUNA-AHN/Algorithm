# 자카드 유사도 : 두 집합 A, B => J(A, B) : 교집합 크기 / 합집합 크기
# 두 글자씩 끊어 다중 집합의 원소, 영문으로만 이루어지지 않는 경우 버림
# 대소문자 차이 무시
# 65536
def solution(str1, str2):
    import math
    n = u = 0
    check1 = dict()
    check2 = dict()
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            check1.setdefault(str1[i:i+2].lower(), 0)
            check1[str1[i:i+2].lower()] += 1
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            # 이미 값이 있는 친구들을 더해줄 필요가 있는지.. 있지.. 
            check2.setdefault(str2[i:i+2].lower(), 0)
            check2[str2[i:i+2].lower()] += 1
    print(check1, check2)
    for i in check1.keys():
        # 둘 다에 존재한다면 => 더 큰 값으로 합집합에 더해주기 , 교집합
        if i in check2.keys():
            u += max(check1[i], check2[i])
            n += min(check1[i], check2[i])
        # 하나에만 존재한다면 => 합집합에 더해주기
        else:
            u += check1[i]
    for i in check2.keys():
        if i not in check1.keys():
            u += check2[i]
    if u == 0:
        return 65536
    else:
        return math.floor(n/u*65536)