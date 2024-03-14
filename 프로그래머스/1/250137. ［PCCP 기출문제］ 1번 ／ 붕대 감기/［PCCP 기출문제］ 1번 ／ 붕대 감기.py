# 14, 16, 18, 20
def solution(bandage, health, attacks):
    answer = 0
    t, x, y = bandage[0], bandage[1], bandage[2] # 시전 시간, 초당, 추가
    now =  health # 현재 체력
    # 이전 공격 시간과 현재 공격 시간 사이 값
    # 0-2 : 1회복 = 데미지 / 2-9 : 6회복 / 9-10 : 0회복 
    last = 0
    for time, d in attacks:
        # 연속 성공 시간
        times = time - last - 1
        bonus = times // t
        # 현재 체력 계산 > max 넘는 경우 max로 변경
        now += times * x + bonus * y
        if now > health:
            now = health
        # 데미지 만큼 감소, 마지막 공격 타임
        now -= d
        last = time
        # 죽었는지 체크 => 죽었으면 break
        if now <= 0:
            now = -1
            break
    return now