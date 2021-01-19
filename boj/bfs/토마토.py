from collections import deque
import sys

M, N, = map(int, input().split())

warehouse = []
for _ in range(N):
    warehouse.append(list(map(int, input().split())))

rare = 0
for m in range(M):
    for n in range(N):
        if warehouse[n][m] == 0:
            rare += 1
if rare == 0:
    print(0)
    sys.exit(0)

deq = deque()
for m in range(M):
    for n in range(N):
        if warehouse[n][m] == 1:
            deq.append([n, m])

day = 0
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
while rare != 0 and deq:
    day += 1
    n = len(deq)
    for _ in range(n):
        pos = deq.popleft()
        for d in range(4):
            next_x = pos[1] + dir_x[d]
            next_y = pos[0] + dir_y[d]
            if 0 <= next_x < M and 0 <= next_y < N and warehouse[next_y][next_x] == 0:
                warehouse[next_y][next_x] = 1
                rare -= 1
                deq.append([next_y, next_x])

if rare == 0:
    print(day)
else:
    print(-1)
