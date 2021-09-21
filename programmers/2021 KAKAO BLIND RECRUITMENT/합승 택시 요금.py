# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
import sys

# 노드의 개수가 커지면 heapq를 이용하는 것이 유리하다.
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
    return d


def solution(n, s, a, b, fares):
    INF = sys.maxsize
    graph = [[INF] * n for _ in range(n)]
    for r in fares:
        graph[r[0] - 1][r[1] - 1] = r[2]
    dl = list()
    for i in range(n):
        dl.append(dijkstra(i + 1, n, graph))
    candi = list()
    for tf in range(n):
        candi.append(dl[s - 1][tf] + dl[tf][a - 1] + dl[tf][b - 1])
    answer = min(candi)
    return answer
