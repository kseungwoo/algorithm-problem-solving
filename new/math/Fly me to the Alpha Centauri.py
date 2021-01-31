import sys

T = int(sys.stdin.readline().strip())

seq = 0
distances = []
for _ in range(T):
    start, end = map(int, sys.stdin.readline().strip().split())
    distances.append((end - start, seq))
    seq += 1

distances.sort(key=lambda x: x[0])
    
move = 1
dp = [0, 1]

answer = []
for i in range(len(distances)):
    while dp[-1] < distances[i][0]:
        move += 1
        if move % 2 == 1:
            dp.append(move // 2 + 1 + dp[-1])
        else:
            dp.append(move // 2 + dp[-1])
    answer.append([move, distances[i][1]])

answer.sort(key=lambda x: x[1])

for i in range(len(answer)):
    print(answer[i][0])
