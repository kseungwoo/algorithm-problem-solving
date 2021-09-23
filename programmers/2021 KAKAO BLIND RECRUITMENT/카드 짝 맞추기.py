# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

import copy
from collections import deque


def solution(board, r, c):
    answer = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()
    q.append([r, c, 0, -1, board])
    s = set()

    while q:
        r, c, act, sel, board = q.popleft()
        if sum(map(sum, board)) == 0:
            answer = act
            break
        if (r, c, sel, tuple(tuple(i) for i in board)) in s:
            continue
        else:
            s.add((r, c, sel, tuple(tuple(i) for i in board)))

        # enter
        if board[r][c] != 0:
            if sel == -1:
                pb = copy.deepcopy(board)
                pb[r][c] = 0
                q.append([r, c, act + 1, board[r][c], pb])
            elif sel == board[r][c]:
                pb = copy.deepcopy(board)
                pb[r][c] = 0
                q.append([r, c, act + 1, -1, pb])

        # move
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr <= 3 and 0 <= nc <= 3:
                pb = copy.deepcopy(board)
                q.append([nr, nc, act + 1, sel, pb])

        # ctrl+move
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr <= 3 and 0 <= nc <= 3:
                while 0 <= nr + dr[d] <= 3 and 0 <= nc + dc[d] <= 3 and board[nr][nc] == 0:
                    nr += dr[d]
                    nc += dc[d]
                if not (nr == r and nc == c):
                    pb = copy.deepcopy(board)
                    q.append([nr, nc, act + 1, sel, pb])

    return answer
