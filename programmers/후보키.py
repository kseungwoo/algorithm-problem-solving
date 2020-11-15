# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from itertools import combinations


def minimality(answer_list, candi):
    for i in answer_list:
        if len(set(list(i) + list(candi))) == len(candi):
            return False
    return True


def solution(relation):
    answer_list = []
    candi_list = []
    combi_list = [n for n in range(len(relation[0]))]
    for n in range(1, len(combi_list) + 1):
        for m in list(combinations(combi_list, n)):
            candi_list.append(m)
    for i in candi_list:
        # Uniqueness
        table = ["" for _ in range(len(relation))]
        for j in i:
            for k in range(len(relation)):
                table[k] += relation[k][j]
        if len(set(table)) == len(relation):
            # Minmality
            if minimality(answer_list, i):
                answer_list.append(i)
    return len(answer_list)