# 4, 9, 12
def solution(storey):
    answer = 0
    count = 0
    while storey:
        if storey % (10 ** (count + 2)) // (10 ** count) >= 55:
            now = storey % (10 ** (count + 2)) // (10 ** count)
            # if now >= 92:
            #     answer += 100 - now
            #     storey += (100 - now) * (10 ** count)
            # else:
            now = now % 10
            if now >= 5:
                storey += (10 - now) * (10 ** count)
                answer += 10 - now
            else:
                answer += now
                storey -= now * (10 ** count)
                print('here')
        else:
            if storey % (10 ** (count + 1)):
                now = storey % (10 ** (count + 1)) // (10 ** count)
            else:
                now  = 0
            if now >= 6:
                answer += 10 - now
                storey += (10 - now) * (10 ** count)
            else:
                answer += now
                storey -= now * (10 ** count)
        count += 1
        
    return answer