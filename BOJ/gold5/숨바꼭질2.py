import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

q = deque()
visited = [0 for _ in range(100001)]
q.append((N, K, 0))
while q:
    N, K, t = q.popleft()
    visited[N] = 1
    if N == K:
        print(t)
        count = 1
        break
    t += 1
    if N - 1 >= 0 and visited[N - 1] == 0:
        q.append((N - 1, K, t))
    if N + 1 <= 100000 and visited[N + 1] == 0:
        q.append((N + 1, K, t))
    if N * 2 <= 100000 and visited[N * 2] == 0:
        q.append((N * 2, K, t))

while q:
    N, K, qt = q.popleft()
    if qt > t:
        break
    if N == K:
        count += 1

print(count)
