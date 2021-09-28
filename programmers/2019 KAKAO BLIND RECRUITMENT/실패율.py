# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from bisect import bisect_right, bisect_left


def solution(N, stages):
    stages.sort()
    d = dict()
    for n in range(1, N + 1):
        if (len(stages) - bisect_left(stages, n)) == 0:
            d[n] = 0
        else:
            d[n] = (bisect_right(stages, n) - bisect_left(stages, n)) / (len(stages) - bisect_left(stages, n))
    answer = sorted(d, key=lambda x: d[x], reverse=True)
    return answer
