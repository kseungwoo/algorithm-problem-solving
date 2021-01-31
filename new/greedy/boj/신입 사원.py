import sys
# Brute-Force -> combination(n^2)
# Greedy -> sort (nlogn) + min (n)
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    scores = []
    for _ in range(N):
        scores.append(list(map(int, sys.stdin.readline().strip().split())))

    passed = N
    scores.sort(key=lambda x: x[0])
    min_score = scores[0][1]
    for i in range(1, N):
        if min_score < scores[i][1]:
            passed -= 1
        else:
            min_score = scores[i][1]
    print(passed)
