# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
import re
from functools import cmp_to_key


def compare(x, y):
    if x[0].lower() > y[0].lower():
        return 1
    elif x[0].lower() == y[0].lower():
        if int(x[1]) > int(y[1]):
            return 1
        elif int(x[1]) < int(y[1]):
            return -1
        else:
            return 0
    else:
        return -1


def solution(files):
    HNT = []
    for file in files:
        NUMBER = list(re.findall("\d+", file))[0]
        HEAD = file[:file.find(NUMBER)]
        TAIL = file[len(NUMBER + HEAD):]
        HNT.append([HEAD, NUMBER, TAIL])
    HNT = sorted(HNT, key=cmp_to_key(compare))
    answer = []
    for i in HNT:
        answer.append(''.join(i))
    return answer
