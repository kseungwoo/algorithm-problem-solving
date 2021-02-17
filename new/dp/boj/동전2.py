# 각각의 값과 경우의 수를 고려함 . Brute force에 가까운 방식
# import sys
# import copy
#
# n, k = map(int, sys.stdin.readline().strip().split())
#
# dp = [10001 for _ in range(k + 1)]
# coin_list = list(set([int(sys.stdin.readline().strip()) for _ in range(n)]))
# count = 0
# next_list = copy.deepcopy(coin_list)
# while len(next_list) != 0:
#     count += 1
#     for i in range(len(next_list) - 1, -1, -1):
#         next_ = next_list[i]
#         del next_list[i]
#         if next_ == k:
#             print(count)
#             sys.exit(0)
#         elif next_ < k and dp[next_] > count:
#             dp[next_] = count
#             for coin in coin_list:
#                 if coin + next_ <= k:
#                     next_list.append(coin + next_)
#
# print(-1)


# DP 풀이. 각각의 동전들은 서로의 조합에 대해서 전혀 모름. 관여하지 않음. 오로지 DP 내부의 값을 통해서만 비교하여 값을 갱신함.
# 서로 관여하지 않고 저장된 DP 데이터에만 의존하여 최소한의 Time Complexity 내에서 최선의 값을 갱신하여 도출해 냄.
import sys
r = sys.stdin.readline

N, K = map(int, r().split())
coins = sorted([int(r()) for _ in range(N)])

arr = [10001] * (K+1)
arr[0] = 0

for i in range(N):
    for j in range(coins[i], K+1):
        arr[j] = min(arr[j], arr[j-coins[i]] + 1)

arr[-1] = arr[-1] if arr[-1] != 10001 else -1
print(arr[-1])

