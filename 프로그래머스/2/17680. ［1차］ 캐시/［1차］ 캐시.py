# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램
# cacheSize : 캐시 크기 / cities : 도시 이름 배열 -> 영문자, 대소문자 구분 X  : 대소문자 체크
# cache hit 1 / cache miss 3
# 캐시 크기 => 기억하는 국가 개수, 가장 오래전에 참조된 항목 삭제
def solution(cacheSize, cities):
    answer = 0
    cache = dict()
    now_cache = dict()
    for i in range(len(cities)):
        if cities[i].lower() in now_cache:
            answer += 1
        else:
            answer += 5
            
        cache.setdefault(cities[i].lower(), 0)
        cache[cities[i].lower()] = i
        now_cache = dict(sorted(cache.items(), key = lambda x:x[1], reverse = True)[:cacheSize]).keys()

    return answer