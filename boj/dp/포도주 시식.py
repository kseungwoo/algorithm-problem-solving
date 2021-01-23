import sys

n = int(input())
arr = []
for _ in range(n):
    i = int(input())
    arr.append(i)

if n == 1:
    print(arr[0])
    sys.exit(0)

dp = [[0, 0] for _ in range(n)]
dp[0][1] = arr[0]
dp[1][0] = arr[0]
dp[1][1] = arr[0] + arr[1]

for s in range(2, n):
    # ---XO -> arr[s]+dp[s-1][0]
    # --XOO -> arr[s]+arr[s-1]+dp[s-2][0]
    dp[s][1] = max(arr[s] + dp[s - 1][0], arr[s] + arr[s - 1] + dp[s - 2][0])
    # --OX -> dp[s - 1][1]
    # --XX -> dp[s - 1][0]
    dp[s][0] = max(dp[s - 1][0], dp[s - 1][1])
    
print(max(dp[n - 1][1], dp[n - 1][0]))
