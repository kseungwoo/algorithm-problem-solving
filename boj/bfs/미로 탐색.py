# DFS -> BFS
# input -> sys.stdin.readline(+.strip()-delete '\n')
# when the case become queue[0] visited check -> visited check before append to queue
# deepcopy -> don't have to deepcopy because it is bfs and so we don't have to take 2 dimensional array to an argument of queue
# deepcopy - bfs(x) dfs(o)
# use deque not list when we use queue

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().strip().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
queue = deque([])
queue.append([0, 0, 1])
miro[0][0] = 0
dir_r = [-1, 1, 0, 0]
dir_c = [0, 0, 1, -1]
while queue:
    now = queue[0]
    queue.popleft()
    if now[0] == N - 1 and now[1] == M - 1:
        print(now[2])
        break
    for i in range(4):
        r = now[0] + dir_r[i]
        c = now[1] + dir_c[i]
        if 0 <= r <= N - 1 and 0 <= c <= M - 1 and miro[r][c] == 1:
            miro[r][c] = 0
            queue.append([r, c, now[2] + 1])
