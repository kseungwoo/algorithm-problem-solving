import sys

sys.setrecursionlimit(100000)
dir_y = [1, -1, 0, 0]
dir_x = [0, 0, 1, -1]


def dfs(pos_y, pos_x):
    above_water_zone[pos_y][pos_x] = 0
    for d in range(4):
        next_y = pos_y + dir_y[d]
        next_x = pos_x + dir_x[d]
        if 0 <= next_y < N and 0 <= next_x < N:
            if above_water_zone[next_y][next_x] == 1:
                dfs(next_y, next_x)
    return


N = int(sys.stdin.readline().strip())
location = []
for _ in range(N):
    location.append(list(map(int, sys.stdin.readline().strip().split())))

max_height = 0
for y in range(N):
    for x in range(N):
        if max_height < location[y][x]:
            max_height = location[y][x]

answer_candidates = []

for h in range(0, max_height + 1):
    above_water_zone = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if location[y][x] > h:
                above_water_zone[y][x] = 1

    n = 0
    for y in range(N):
        for x in range(N):
            if above_water_zone[y][x] == 1:
                n += 1
                dfs(y, x)
    answer_candidates.append(n)

print(max(answer_candidates))