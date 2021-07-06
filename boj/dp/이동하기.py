import sys

N, M = map(int, sys.stdin.readline().strip().split())

candy_map = []
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for _ in range(N):
    candy_map.append(list(map(int, sys.stdin.readline().strip().split())))

for n in range(1, N + 1):
    for m in range(1, M + 1):
        dp[n][m] = max(dp[n - 1][m - 1], dp[n - 1][m], dp[n][m - 1]) + candy_map[n - 1][m - 1]

print(dp[N][M])
