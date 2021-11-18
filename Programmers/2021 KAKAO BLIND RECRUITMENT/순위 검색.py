# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
import itertools
import bisect


def solution(info, query):
    answer = []
    # info
    d = dict()
    for i in info:
        i = i.split(' ')
        for n in range(5):
            for k in list(itertools.combinations(i[:-1], n)):
                if k in d:
                    d[k].append(int(i[-1]))
                else:
                    d[k] = [int(i[-1])]
    for k in d.keys():
        d[k] = sorted(d[k])

    # query
    for q in query:
        q = q.split(' and ')
        q.extend(q.pop().split(' '))
        q = tuple(e for e in q if e != '-')
        if q[:-1] in d:
            res = d[q[:-1]]
            answer.append(len(res) - bisect.bisect_left(res, int(q[-1])))
        else:
            answer.append(0)

    return answer
