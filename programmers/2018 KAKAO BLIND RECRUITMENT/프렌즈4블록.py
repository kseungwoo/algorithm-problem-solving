import copy
from collections import deque


def pop(m, n, board):
    new_board = copy.deepcopy(board)
    isFinished = True
    for r in range(m - 1):
        for c in range(n - 1):
            if board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1] != 0:
                new_board[r][c] = new_board[r + 1][c] = new_board[r][c + 1] = new_board[r + 1][c + 1] = 0
                isFinished = False
    return new_board, isFinished


def blank_fill(m, n, b):
    dq = deque()
    for c in range(n):
        for r in range(m):
            if b[r][c] != 0:
                dq.append(b[r][c])
        for _ in range(m - len(dq)):
            dq.appendleft(0)
        for r in range(m):
            b[r][c] = dq[r]
        dq.clear()
    return b


def solution(m, n, board):
    b = [list(row) for row in board]
    while True:
        b, isFinished = pop(m, n, b)
        if isFinished:
            return sum(row.count(0) for row in b)
        b = blank_fill(m, n, b)
