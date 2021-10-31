import sys

N, M, K = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
B = [[5 for _ in range(N)] for _ in range(N)]
trees = []
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().strip().split())
    trees.append((y - 1, x - 1, z))
for _ in range(K):
    trees.sort(key=lambda t: t[2])
    for i, v in enumerate(trees):
        dead = []
        r, c, old = v[0], v[1], v[2]
        if old > B[r][c]:
            dead.append((r, c, old, i))
        else:
            B[r][c] -= old
            trees[i] = (r, c, old + 1)
    for n in range(len(dead) - 1, -1, -1):
        r, c, old, i = dead[n][0], dead[n][1], dead[n][2], dead[n][3]
        del trees[i]
        B[r][c] += old // 2
    dy, dx = (-1, -1, -1, 0, 1, 1, 1, 0), (-1, 0, 1, 1, 1, 0, -1, -1)
    for r, c, old in trees:
        new_trees = []
        if old % 5 == 0:
            for d in range(8):
                nr, nc = r + dy[d], c + dx[d]
                if 0 <= nr < N and 0 <= nc < N:
                    new_trees.append((nr, nc, 1))
    trees.extend(new_trees)
    for r in range(N):
        for c in range(N):
            B[r][c] += A[r][c]
print(len(trees))
