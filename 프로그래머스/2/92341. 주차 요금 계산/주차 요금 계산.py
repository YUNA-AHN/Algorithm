# 누적시간 기준 - 기본 시간 (180분, 500원) / 10분에 600원 
# 출차된 내역이 없다면 23:59 출차
# 초과 시간이 단위시간으로 나누어지지 않으면 올림!
# 차량번호 작은 순으로 주차요금 배열
def solution(fees, records):
    import math
    answer = dict()
    times = dict()
    basic, basic_fee, more, more_fee = fees[0], fees[1], fees[2], fees[3]
    for record in records:
        check = record.split()
        if check[2] == "IN":
            # 차번호 : (입차시간, 총시간, 입차여부)
            times.setdefault(check[1], [check[0], 0, 'IN'])
            times[check[1]][0] = check[0]
            times[check[1]][2] = 'IN'
        else:
            times[check[1]][2] = 'OUT'
            start = int(times[check[1]][0][:2]) * 60 + int(times[check[1]][0][3:])
            end = int(check[0][:2]) * 60 + int(check[0][3:])
            times[check[1]][1] += end - start

    # 마지막까지 in인 경우 체크
    # 딕셔너리로 받아서 => 마지막에 in인 경우 체크..? => 마지막에 계산
    for key, value in times.items():
        if value[2] == "IN":
            start = int(value[0][:2]) * 60 + int(value[0][3:])
            end = 23 * 60 + 59
            total = value[1] + end - start
        else:
            total = value[1]
        # 계산하기
        total_fee = 0
        if total > basic :
            total_fee += basic_fee
            total -= basic
            total_fee += math.ceil(total / more) * more_fee
        else:
            total_fee = basic_fee
        answer[key] = total_fee
    
    return list(dict(sorted(answer.items(), key = lambda x: x[0])).values())