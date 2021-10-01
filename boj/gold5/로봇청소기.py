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
    if 0 <= r + dir[(d + 3) % 4][0] < N and 0 <= c + dir[(d + 3) % 4][1] < M and mp[r + dir[(d + 3) % 4][0]][c + dir[(d + 3) % 4][1]] == 0:
        d = (d + 3) % 4
        r, c = r + dir[d][0], c + dir[d][1]
        mp[r][c] = 2
        count += 1
        continue
    else:
        d = (d + 3) % 4
    if 0 <= r + dir[(d + 3) % 4][0] < N and 0 <= c + dir[(d + 3) % 4][1] < M and mp[r + dir[(d + 3) % 4][0]][c + dir[(d + 3) % 4][1]] == 0:
        d = (d + 3) % 4
        r, c = r + dir[d][0], c + dir[d][1]
        mp[r][c] = 2
        count += 1
        continue
    else:
        d = (d + 3) % 4
    if 0 <= r + dir[(d + 3) % 4][0] < N and 0 <= c + dir[(d + 3) % 4][1] < M and mp[r + dir[(d + 3) % 4][0]][c + dir[(d + 3) % 4][1]] == 0:
        d = (d + 3) % 4
        r, c = r + dir[d][0], c + dir[d][1]
        mp[r][c] = 2
        count += 1
        continue
    else:
        d = (d + 3) % 4
    if 0 <= r + dir[(d + 3) % 4][0] < N and 0 <= c + dir[(d + 3) % 4][1] < M and mp[r + dir[(d + 3) % 4][0]][c + dir[(d + 3) % 4][1]] == 0:
        d = (d + 3) % 4
        r, c = r + dir[d][0], c + dir[d][1]
        mp[r][c] = 2
        count += 1
        continue
    else:
        d = (d + 3) % 4

    if 0 <= r + dir[(d + 2) % 4][0] < N and 0 <= c + dir[(d + 2) % 4][1] < M and mp[r + dir[(d + 2) % 4][0]][c + dir[(d + 2) % 4][1]] == 2:
        r, c = r + dir[(d + 2) % 4][0], c + dir[(d + 2) % 4][1]
        continue
    else:
        break

print(count)