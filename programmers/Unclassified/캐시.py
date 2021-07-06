# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(cacheSize, cities):
    answer = 0
    cache = [str(i) for i in range(cacheSize)]
    cities = [c.lower() for c in cities]
    if cacheSize == 0:
        return 5 * len(cities)
    for n in range(len(cities)):
        if cities[n] not in cache:
            answer += 5
            del cache[0]
            cache.append(cities[n])
        else:
            answer += 1
            del cache[cache.index(cities[n])]
            cache.append(cities[n])
    return answer
