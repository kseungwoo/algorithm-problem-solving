import sys

N = int(sys.stdin.readline().strip())
cost = []
for _ in range(N):
    r, g, b = map(int, sys.stdin.readline().strip().split())
    cost.append([r, g, b])

dp = [[0, 0, 0] for _ in range(N)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for n in range(1, N):
    dp[n][0] = cost[n][0] + min(dp[n - 1][1], dp[n - 1][2])
    dp[n][1] = cost[n][1] + min(dp[n - 1][0], dp[n - 1][2])
    dp[n][2] = cost[n][2] + min(dp[n - 1][0], dp[n - 1][1])

print(min(min(dp[N - 1][0], dp[N - 1][1]), dp[N - 1][2]))
