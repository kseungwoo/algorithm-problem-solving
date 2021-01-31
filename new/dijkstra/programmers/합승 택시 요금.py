# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

import sys


def dijkstra(K, V, graph):
    INF = sys.maxsize
    s = [False] * V
    d = [INF] * V
    d[K - 1] = 0
    while True:
        m = INF
        N = -1
        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j
        if m == INF:
            break
        s[N] = True
        for j in range(V):
            if s[j]:
                continue
            via = d[N] + min(graph[N][j], graph[j][N])  # 출발 / 도착 구분 없음
            if d[j] > via:
                d[j] = via
    for i in range(len(d)):
        if d[i] == INF:
            d[i] = -1
    return d


def solution(n, s, a, b, fares):
    dijkstra_results = []
    INF = sys.maxsize
    graph = [[INF] * n for _ in range(n)]
    for fare in fares:
        graph[fare[0] - 1][fare[1] - 1] = fare[2]
    answer = 0
    for i in range(1, n + 1):
        dijkstra_results.append(dijkstra(i, n, graph))

    answer = INF
    for i in range(1, n + 1):
        transfer = dijkstra_results[s - 1][i - 1]
        to_a = dijkstra_results[s - 1][i - 1] + dijkstra_results[i - 1][a - 1]
        to_b = dijkstra_results[s - 1][i - 1] + dijkstra_results[i - 1][b - 1]
        if transfer != -1 and to_a != -1 and to_b != -1:
            answer = min(answer, to_a + to_b - transfer)

    return answer