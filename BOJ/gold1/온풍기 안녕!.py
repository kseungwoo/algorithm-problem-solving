import sys
from collections import deque


def valid(R, C, x, y, visited):
    return 0 <= x < R and 0 <= y < C and visited[x][y] == 0


def bfs(R, C, machine, imap, wall):
    dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)
    visited = [[0 for _ in range(C)] for _ in range(R)]
    q = deque([(machine[0] + dr[machine[2] - 1], machine[1] + dc[machine[2] - 1], machine[2], 5)])
    while q:
        x, y, d, K = q.popleft()
        imap[x][y] += K
        if K == 1:
            continue
        if d == 1:
            if valid(R, C, x - 1, y + 1, visited) and not ((x, y) in wall[0]) and not ((x - 1, y) in wall[1]):
                visited[x - 1][y + 1] = 1
                q.append((x - 1, y + 1, d, K - 1))
            if valid(R, C, x, y + 1, visited) and not ((x, y) in wall[1]):
                visited[x][y + 1] = 1
                q.append((x, y + 1, d, K - 1))
            if valid(R, C, x + 1, y + 1, visited) and not ((x + 1, y) in wall[0]) and not ((x + 1, y) in wall[1]):
                visited[x + 1][y + 1] = 1
                q.append((x + 1, y + 1, d, K - 1))
        elif d == 2:
            if valid(R, C, x - 1, y - 1, visited) and not ((x, y) in wall[0]) and not ((x - 1, y - 1) in wall[1]):
                visited[x - 1][y - 1] = 1
                q.append((x - 1, y - 1, d, K - 1))
            if valid(R, C, x, y - 1, visited) and not ((x, y - 1) in wall[1]):
                visited[x][y - 1] = 1
                q.append((x, y - 1, d, K - 1))
            if valid(R, C, x + 1, y - 1, visited) and not ((x + 1, y) in wall[0]) and not (
                    (x + 1, y - 1) in wall[1]):
                visited[x + 1][y - 1] = 1
                q.append((x + 1, y - 1, d, K - 1))
        elif d == 3:
            if valid(R, C, x - 1, y - 1, visited) and not ((x, y - 1) in wall[0]) and not ((x, y - 1) in wall[1]):
                visited[x - 1][y - 1] = 1
                q.append((x - 1, y - 1, d, K - 1))
            if valid(R, C, x - 1, y, visited) and not ((x, y) in wall[0]):
                visited[x - 1][y] = 1
                q.append((x - 1, y, d, K - 1))
            if valid(R, C, x - 1, y + 1, visited) and not ((x, y + 1) in wall[0]) and not ((x, y) in wall[1]):
                visited[x - 1][y + 1] = 1
                q.append((x - 1, y + 1, d, K - 1))
        else:
            if valid(R, C, x + 1, y - 1, visited) and not ((x, y - 1) in wall[1]) and not (
                    (x + 1, y - 1) in wall[0]):
                visited[x + 1][y - 1] = 1
                q.append((x + 1, y - 1, d, K - 1))
            if valid(R, C, x + 1, y, visited) and not ((x + 1, y) in wall[0]):
                visited[x + 1][y] = 1
                q.append((x + 1, y, d, K - 1))
            if valid(R, C, x + 1, y + 1, visited) and not ((x, y) in wall[1]) and not ((x + 1, y + 1) in wall[0]):
                visited[x + 1][y + 1] = 1
                q.append((x + 1, y + 1, d, K - 1))


def calculate_increase(R, C, machines, wall):
    imap = [[0 for _ in range(C)] for _ in range(R)]
    for machine in machines:
        bfs(R, C, machine, imap, wall)
    return imap


def spread(R, C, tmap, wall):
    smap = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            next_ = []
            if 0 <= r - 1 < R and 0 <= c < C and not ((r, c) in wall[0]):
                next_.append((r - 1, c))
            if 0 <= r < R and 0 <= c + 1 < C and not ((r, c) in wall[1]):
                next_.append((r, c + 1))
            if 0 <= r + 1 < R and 0 <= c < C and not ((r + 1, c) in wall[0]):
                next_.append((r + 1, c))
            if 0 <= r < R and 0 <= c - 1 < C and not ((r, c - 1) in wall[1]):
                next_.append((r, c - 1))
            for nr, nc in next_:
                sub = tmap[nr][nc] - tmap[r][c]
                if sub > 0:
                    smap[r][c] += sub // 4
                else:
                    smap[r][c] += -(-sub // 4)
    for r in range(R):
        for c in range(C):
            tmap[r][c] += smap[r][c]


def decrease(R, C, tmap):
    for r in range(R):
        for c in range(C):
            if (r == 0 or r == R - 1) or (c == 0 or c == C - 1):
                if tmap[r][c] > 0:
                    tmap[r][c] -= 1


def solution():
    R, C, K = map(int, sys.stdin.readline().strip().split())
    m = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]
    machines = [(r, c, m[r][c]) for r in range(R) for c in range(C) if 1 <= m[r][c] <= 4]
    inspects = [(r, c) for r in range(R) for c in range(C) if m[r][c] == 5]
    wall = [set(), set()]
    W = int(sys.stdin.readline().strip())
    for _ in range(W):
        x, y, t = map(int, sys.stdin.readline().strip().split())
        wall[t].add((x - 1, y - 1))
    tmap = [[0 for _ in range(C)] for _ in range(R)]
    choco = 1
    increase = calculate_increase(R, C, machines, wall)
    while choco <= 100:
        for r in range(R):
            for c in range(C):
                tmap[r][c] += increase[r][c]
        spread(R, C, tmap, wall)
        decrease(R, C, tmap)
        if min(tmap[r][c] for r, c in inspects) < K:
            choco += 1
        else:
            print(choco)
            exit(0)
    print(choco)


solution()
