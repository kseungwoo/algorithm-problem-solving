# 출처 : https://www.acmicpc.net/problem/2178
# DFS -> BFS
# input -> sys.stdin.readline(+.strip()-delete '\n')
# when the case become queue[0] visited check -> visited check before append to queue
# deepcopy -> don't have to deepcopy because it is bfs and so we don't have to take 2 dimensional array to an argument of queue
# deepcopy - bfs(x) dfs(o)
# use Deque not list when we use queue

# DFS -> BFS
# input -> sys.stdin.readline(+.strip()-delete '\n')
# when the case become queue[0] visited check -> visited check before append to queue
# deepcopy -> don't have to deepcopy because it is bfs and so we don't have to take 2 dimensional array to an argument of queue
# deepcopy - bfs(x) dfs(o)
# use Deque not list when we use queue

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().strip().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[0 for _ in range(M)] for _ in range(N)]
q = deque()
visited[0][0] = 1
q.append([0, 0, 1])
answer = -1
while q:
    r, c, move = q.popleft()
    if r == N - 1 and c == M - 1:
        answer = move
        break
    for d in range(4):
        next_r = r + dx[d]
        next_c = c + dy[d]
        if 0 <= next_r < N and 0 <= next_c < M and miro[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
            visited[next_r][next_c] = 1
            q.append([next_r, next_c, move + 1])

print(answer)
