import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
B = [[5 for _ in range(N)] for _ in range(N)]
dy, dx = (-1, -1, -1, 0, 1, 1, 1, 0), (-1, 0, 1, 1, 1, 0, -1, -1)

trees = []
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().strip().split())
    trees.append((x - 1, y - 1, z))
trees = deque(sorted(trees, key=lambda t: t[2]))
for k in range(K):
    dead = []
    replace_tree = deque()
    for r, c, old in trees:
        if old > B[r][c] + A[r][c] * k:
            dead.append((r, c, old))
        else:
            replace_tree.append((r, c, old + 1))
            B[r][c] -= old
    trees = replace_tree
    for r, c, old in dead:
        B[r][c] += old // 2
    i = 0
    while i < len(trees):
        r, c, old = trees[i][0], trees[i][1], trees[i][2]
        if old % 5 == 0:
            for d in range(8):
                nr, nc = r + dy[d], c + dx[d]
                if 0 <= nr < N and 0 <= nc < N:
                    trees.appendleft((nr, nc, 1))
                    i += 1
        i += 1
print(len(trees))
