from collections import deque


def solution(rows, columns, queries):
    res = []
    M = [[columns * (r - 1) + c for c in range(1, columns + 1)] for r in range(1, rows + 1)]
    for r1, c1, r2, c2 in queries:
        q = deque()
        for c in range(c1, c2):
            q.append(M[r1 - 1][c - 1])
        for r in range(r1, r2):
            q.append(M[r - 1][c2 - 1])
        for c in range(c2, c1, -1):
            q.append(M[r2 - 1][c - 1])
        for r in range(r2, r1, -1):
            q.append(M[r - 1][c1 - 1])
        q.appendleft(q.pop())
        res.append(min(q))
        for c in range(c1, c2):
            M[r1 - 1][c - 1] = q.popleft()
        for r in range(r1, r2):
            M[r - 1][c2 - 1] = q.popleft()
        for c in range(c2, c1, -1):
            M[r2 - 1][c - 1] = q.popleft()
        for r in range(r2, r1, -1):
            M[r - 1][c1 - 1] = q.popleft()

    return res
