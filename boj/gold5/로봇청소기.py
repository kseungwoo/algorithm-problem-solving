import sys

N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))
mp = []
for _ in range(N):
    mp.append(list(map(int, sys.stdin.readline().strip().split())))
count = 1
mp[r][c] = 2

while True:
    done = False
    for _ in range(4):
        next_r, next_c = r + dir[(d + 3) % 4][0], c + dir[(d + 3) % 4][1]
        if 0 <= next_r < N and 0 <= next_c < M and mp[next_r][next_c] == 0:
            d = (d + 3) % 4
            r, c = next_r, next_c
            mp[r][c] = 2
            count += 1
            done = True
            break
        else:
            d = (d + 3) % 4

    if done:
        continue

    next_r, next_c = r + dir[(d + 2) % 4][0], c + dir[(d + 2) % 4][1]
    if 0 <= next_r < N and 0 <= next_c < M and mp[next_r][next_c] == 2:
        r, c = next_r, next_c
        continue
    else:
        break

print(count)
