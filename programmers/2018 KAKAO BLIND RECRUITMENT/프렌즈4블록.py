import copy
from collections import deque


def pop(m, n, board):
    new_board = copy.deepcopy(board)
    isPopped = False
    for r in range(m - 1):
        for c in range(n - 1):
            if board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1] != 0:
                new_board[r][c] = new_board[r + 1][c] = new_board[r][c + 1] = new_board[r + 1][c + 1] = 0
                isPopped = True
    return new_board, isPopped


def blank_fill(m, n, b):
    l = deque()
    for c in range(n):
        for r in range(m):
            if b[r][c] != 0:
                l.append(b[r][c])
        for _ in range(m - len(l)):
            l.appendleft(0)
        for r in range(m):
            b[r][c] = l[r]
        l.clear()
    return b


def solution(m, n, board):
    b = list()
    for row in board:
        b.append(list(row))
    while True:
        b, isPopped = pop(m, n, b)
        if not isPopped:
            count = 0
            for r in range(m):
                for c in range(n):
                    if b[r][c] == 0:
                        count += 1
            return count
        b = blank_fill(m, n, b)
