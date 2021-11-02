import sys


def gerry(N, A, x, y, d1, d2):
    M = [[0 for _ in range(N)] for _ in range(N)]
    # 경계선 5로 표시
    for i in range(d1 + 1):
        if not (0 <= x + i < N and 0 <= y - i < N):
            return -1
        M[y - i][x + i] = 5
    for i in range(d2 + 1):
        if not (0 <= x + i < N and 0 <= y + i < N):
            return -1
        M[y + i][x + i] = 5
    for i in range(d2 + 1):
        if not (0 <= x + d1 + i < N and 0 <= y - d1 + i < N):
            return -1
        M[y - d1 + i][x + d1 + i] = 5
    for i in range(d1 + 1):
        if not (0 <= x + d2 + i < N and 0 <= y + d2 - i < N):
            return -1
        M[y + d2 - i][x + d2 + i] = 5

    # 1, 2, 3, 4 구역 칠하기
    for c in range(0, x + d1 + 1):
        for r in range(0, y):
            if M[r][c] == 5:
                break
            M[r][c] = 1
    for r in range(0, y - d1 + d2 + 1):
        for c in range(N - 1, x + d1, -1):
            if M[r][c] == 5:
                break
            M[r][c] = 2
    for c in range(0, x + d2 + 2):
        for r in range(N - 1, y - 1, -1):
            if M[r][c] == 5:
                break
            M[r][c] = 3
    for r in range(y - d1 + d2 + 1, N):
        for c in range(N - 1, x + d2 - 1, -1):
            if M[r][c] == 5:
                break
            M[r][c] = 4
    # 인구 수 구하기
    res = [0, 0, 0, 0, 0]
    for r in range(N):
        for c in range(N):
            if M[r][c] in (0, 5):
                res[0] += A[r][c]
            else:
                res[M[r][c]] += A[r][c]
    return max(res) - min(res)


def solution():
    N = int(sys.stdin.readline().strip())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    gerry(N, A, 1, 3, 2, 2)
    result = []
    for x in range(N):
        for y in range(N):
            for d1 in range(1, int(N * 1.414) + 1):
                for d2 in range(1, int(N * 1.414) + 1):
                    element = gerry(N, A, x, y, d1, d2)
                    if element == -1:
                        break
                    else:
                        result.append(element)

    print(min(result))


solution()
