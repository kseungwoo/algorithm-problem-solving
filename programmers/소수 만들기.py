# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from itertools import combinations


def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    candi = list(combinations(nums, 3))
    for i in candi:
        if is_prime_number(sum(i)):
            answer += 1
    return answer
