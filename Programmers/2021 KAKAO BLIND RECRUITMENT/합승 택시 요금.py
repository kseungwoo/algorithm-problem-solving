# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
import sys


def solution(n, s, a, b, fares):
    INF = sys.maxsize
    cost = [[INF] * n for _ in range(n)]
    for f in fares:
        cost[f[0] - 1][f[1] - 1] = f[2]
        cost[f[1] - 1][f[0] - 1] = f[2]

    for k in range(n):
        cost[k][k] = 0
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    candi = list()
    for tf in range(n):
        candi.append(cost[s - 1][tf] + cost[tf][a - 1] + cost[tf][b - 1])
    answer = min(candi)

    return answer
