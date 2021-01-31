# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

from itertools import combinations


def solution(orders, course):
    dict1 = {}
    dict2 = {}
    for order in orders:
        order = ''.join(sorted(list(order)))
        for n in course:
            for key in list(combinations(order, n)):
                if key in dict1:
                    dict1[key] += 1
                else:
                    dict1[key] = 1
                if len(key) in dict2:
                    dict2[len(key)] = max(dict2[len(key)], dict1[key])
                else:
                    dict2[len(key)] = dict1[key]
    answer = []
    for key in dict1:
        if dict2[len(key)] == dict1[key] and dict1[key] >= 2:
            answer.append(''.join(key))
    answer.sort()
    return answer
