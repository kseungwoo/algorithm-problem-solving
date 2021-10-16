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

    # 4가지 방향(상,하,좌,우) 정보
    dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
    # 방향 전환 정보
    LT, RT = {0: 3, 1: 2, 2: 0, 3: 1}, {0: 2, 1: 3, 2: 1, 3: 0}
    # t: 시간, hy/hx: 헤드 위치, ty/tx: 테일 위치, d: 방향
    t = hy = hx = ty = tx = d = b[0][0] = 0
    while True:
        # 시간 경과
        t += 1
        # 헤드 움직이기
        hy, hx = hy + dy[d], hx + dx[d]
        # 게임 종료 조건
        if hy < 0 or N <= hy or hx < 0 or N <= hx or b[hy][hx] >= 0:
            print(t)
            exit(0)
        # 사과 존재 유무 체크
        if b[hy][hx] == -1:
            apple = False
        else:
            apple = True
        # 뱀의 헤드 기록
        b[hy][hx] = t
        # 사과가 없었을 경우 꼬리 줄이기
        if not apple:
            for i in range(4):
                ny, nx = ty + dy[i], tx + dx[i]
                if 0 <= ny < N and 0 <= nx < N and b[ny][nx] == b[ty][tx] + 1:
                    b[ty][tx] = -1
                    ty, tx = ny, nx
                    break
        # 방향 전환 해야할 경우
        if q and int(q[0][0]) == t:
            dT = q.popleft()
            if dT[1] == 'L':
                d = LT[d]
            else:
                d = RT[d]


solution()
