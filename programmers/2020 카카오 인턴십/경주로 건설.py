import copy
import math


def solution(board):
    n = len(board)
    dp = [[[math.inf for _ in range(2)] for _ in range(n)] for _ in range(n)]
    s = []
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    s.append((0, 0, 0, -1))
    while s:
        r, c, cost, prev = s.pop()
        if r == n - 1 and c == n - 1:
            continue
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if d == 0 or d == 1:
                cur = 0
            else:
                cur = 1
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                if prev == cur or prev == -1:
                    if cost + 100 <= dp[nr][nc][cur]:
                        s.append((nr, nc, cost + 100, cur))
                        dp[nr][nc][cur] = cost + 100
                else:
                    if cost + 600 <= dp[nr][nc][cur]:
                        s.append((nr, nc, cost + 600, cur))
                        dp[nr][nc][cur] = cost + 600

    answer = min(dp[n - 1][n - 1][0], dp[n - 1][n - 1][1])
    return answer
