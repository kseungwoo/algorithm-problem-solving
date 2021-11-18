import sys
from collections import deque


def bfs(y, x):
    dir_y = [1, 0, -1, 0]
    dir_x = [0, -1, 0, 1]
    deq = deque()
    deq.append([y, x])
    n = 1
    city[y][x] = 0
    while deq:
        pos = deq.popleft()
        for d in range(4):
            next_y = pos[0] + dir_y[d]
            next_x = pos[1] + dir_x[d]
            if 0 <= next_y < N and 0 <= next_x < N and city[next_y][next_x] == 1:
                city[next_y][next_x] = 0
                deq.append([next_y, next_x])
                n += 1
    cities.append(n)
    return


N = int(sys.stdin.readline().strip())

city = []
for _ in range(N):
    city.append(list(map(int, str(sys.stdin.readline().strip()))))

count = 0
cities = []

for y in range(N):
    for x in range(N):
        if city[y][x] == 1:
            bfs(y, x)
            count += 1

cities.sort()

print(count)
for e in range(len(cities)):
    print(cities[e])
