# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
# 기존 다익스트라 변형
# 1. 출발 / 도착점 구분 X
# 2. 중복 되는 경우 O

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
    return d


def solution(N, road, K):
    INF = sys.maxsize
    graph = [[INF] * N for _ in range(N)]
    for r in road:
        graph[r[0] - 1][r[1] - 1] = min(r[2], graph[r[0] - 1][r[1] - 1])  # 중복되는 길 있을 수 있음
    answer = 0
    for d in dijkstra(1, N, graph):
        if d <= K:
            answer += 1
    return answer

# 기존 다익스트라
# import sys


# def dijkstra(K, V, graph):
#     INF = sys.maxsize
#     s = [False] * V
#     d = [INF] * V
#     d[K - 1] = 0
#     while True:
#         m = INF
#         N = -1
#         for j in range(V):
#             if not s[j] and m > d[j]:
#                 m = d[j]
#                 N = j
#         if m == INF:
#             break
#         s[N] = True
#         for j in range(V):
#             if s[j]: continue
#             via = d[N] + graph[N][j] # <- 단방향 | 양방향 -> min(graph[N][j],graph[j][N])
#             if d[j] > via:
#                 d[j] = via
#     return d

# if __name__ == "__main__":
#     V, E = map(int, input().split())
#     K = int(input())
#     INF = sys.maxsize
#     graph = [[INF]*V for _ in range(V)]

#     for _ in range(E):
#         u, v, w = map(int, input().split())
#         graph[u-1][v-1] = w # 중복 O -> graph[u-1][v-1]=min(graph[u-1][v-1],w)

#     for d in dijkstra(K, V, graph):
#         print(d if d != INF else "INF")