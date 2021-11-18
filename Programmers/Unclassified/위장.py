# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenge
def solution(clothes):
    dictionary = dict()
    for c in clothes:
        if dictionary.get(c[1]) is None:
            dictionary[c[1]] = 1
        else:
            dictionary[c[1]] += 1
    answer = 1
    for value in dictionary.values():
        answer *= value + 1
    return answer - 1
