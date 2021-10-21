import sys


def solution():
    N = int(sys.stdin.readline().strip())
    plan = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    dp = [0 for _ in range(N + 1)]

    for i in range(N):
        dp[i + 1] = max(dp[i], dp[i + 1])
        if i + plan[i][0] <= N:
            dp[i + plan[i][0]] = max(dp[i + plan[i][0]], dp[i] + plan[i][1])

    print(dp[N])


solution()
