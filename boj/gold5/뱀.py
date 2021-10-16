import sys
from collections import deque


def solution():
    N = int(sys.stdin.readline().strip())
    b = [[-1 for _ in range(N)] for _ in range(N)]
    K = int(sys.stdin.readline().strip())
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().strip().split())
        b[y - 1][x - 1] = -2
    L = int(sys.stdin.readline().strip())
    q = deque()
    for _ in range(L):
        q.append(tuple(map(str, sys.stdin.readline().strip().split())))
    dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
    LT, RT = {0: 3, 1: 2, 2: 0, 3: 1}, {0: 2, 1: 3, 2: 1, 3: 0}
    t = hy = hx = ty = tx = d = b[0][0] = 0
    while True:
        t += 1
        hy, hx = hy + dy[d], hx + dx[d]
        if hy < 0 or N <= hy or hx < 0 or N <= hx or b[hy][hx] >= 0:
            print(t)
            exit(0)
        if b[hy][hx] == -1:
            apple = False
        else:
            apple = True
        b[hy][hx] = t
        if not apple:
            for i in range(4):
                ny, nx = ty + dy[i], tx + dx[i]
                if 0 <= ny < N and 0 <= nx < N and b[ny][nx] == b[ty][tx] + 1:
                    b[ty][tx] = -1
                    ty, tx = ny, nx
                    break
        if q and int(q[0][0]) == t:
            dT = q.popleft()
            if dT[1] == 'L':
                d = LT[d]
            else:
                d = RT[d]


solution()
