# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from itertools import permutations


def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    n = len(numbers)
    split_num = []
    for i in numbers:
        split_num.append(i)
    prime_candi = []
    for i in range(1, n + 1):
        for j in list(map(''.join, permutations(split_num, i))):
            if int(j) >= 2:
                prime_candi.append(int(j))
    prime_candi = list(set(prime_candi))
    answer = 0
    for i in prime_candi:
        if is_prime_number(i):
            answer += 1
    return answer
