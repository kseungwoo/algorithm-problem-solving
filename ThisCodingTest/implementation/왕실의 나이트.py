import sys

s = str(sys.stdin.readline().strip())

dl = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (1, -2), (-2, -2))
r = int(s[1])
c = ord(s[0]) - 96
count = 0
for d in dl:
    if 1 <= r + d[0] <= 8 and 1 <= c + d[1] <= 8:
        count += 1
print(count)