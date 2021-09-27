import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

q = deque()
visited = [0 for _ in range(100001)]

q.append((N, K, 0))
visited[N] = 1

while q:
    N, K, t = q.popleft()
    if N == K:
        print(t)
        exit(0)
    if N * 2 <= 100000 and visited[N * 2] == 0:
        q.appendleft((N * 2, K, t))
        visited[N * 2] = 1
    t += 1
    if N - 1 >= 0 and visited[N - 1] == 0:
        q.append((N - 1, K, t))
        visited[N - 1] = 1
    if N + 1 <= 100000 and visited[N + 1] == 0:
        q.append((N + 1, K, t))
        visited[N + 1] = 1
