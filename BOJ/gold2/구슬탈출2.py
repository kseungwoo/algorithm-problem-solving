import sys
from collections import deque


def move(Ry, Rx, By, Bx, d, board):
    dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
    # 0: 계속 플레이, 1: 성공(빨간 구슬 들어감), 2: 실패(파란 구슬 들어감)
    J = 0
    oRy, oRx, oBy, oBx = Ry, Rx, By, Bx
    # 빨간 구슬 움직이기
    while True:
        nRy, nRx = Ry + dy[d], Rx + dx[d]
        if board[nRy][nRx] == '#':
            break
        if board[nRy][nRx] == 'O':
            J = 1
        Ry, Rx = nRy, nRx
    # 파란 구슬 움직이기
    while True:
        nBy, nBx = By + dy[d], Bx + dx[d]
        if board[nBy][nBx] == '#':
            break
        if board[nBy][nBx] == 'O':
            J = 2
        By, Bx = nBy, nBx
    # 구슬들이 겹칠 때 예외 처리
    if J == 0 and Ry == By and Rx == Bx:
        if d == 0:
            if oRx < oBx:
                Rx -= 1
            else:
                Bx -= 1
        elif d == 1:
            if oRx < oBx:
                Bx += 1
            else:
                Rx += 1
        elif d == 2:
            if oRy < oBy:
                Ry -= 1
            else:
                By -= 1
        else:
            if oRy < oBy:
                By += 1
            else:
                Ry += 1
    return Ry, Rx, By, Bx, J


def solution():
    N, M = map(int, sys.stdin.readline().strip().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # 초기화하지 않아도 풀리지만, 빨간 구슬 및 파란 구슬이 보드에 존재하지 않는 케이스를 고려하려면 필요할 수도 있음.
    Ry = Rx = By = Bx = -1
    # 빨간 구슬, 파란 구슬 위치 찾기
    for y in range(N):
        for x in range(M):
            if board[y][x] in ('R', 'B'):
                if board[y][x] == 'R':
                    Ry, Rx = y, x
                else:
                    By, Bx = y, x
                board[y][x] = '.'
    # BFS
    q = deque()
    q.append((0, Ry, Rx, By, Bx))
    while q:
        c, Ry, Rx, By, Bx = q.popleft()
        if c >= 10:
            print(-1)
            exit(0)
        for d in range(4):
            nRy, nRx, nBy, nBx, J = move(Ry, Rx, By, Bx, d, board)
            # 계속 플레이
            if J == 0:
                q.append((c + 1, nRy, nRx, nBy, nBx))
            # 성공
            elif J == 1:
                print(c + 1)
                exit(0)
            # 실패
            else:
                continue


solution()
