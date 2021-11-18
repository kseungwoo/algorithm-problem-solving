import sys

n = map(int, sys.stdin.readline().strip().split())
dl = map(str, sys.stdin.readline().strip().split())

r = c = 1
dir = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

for d in dl:
    if 1 <= r + dir[d][0] <= n and 1 <= c + dir[d][1] <= n:
        r += dir[d][0]
        c += dir[d][1]

print("%d %d" % (r, c))
