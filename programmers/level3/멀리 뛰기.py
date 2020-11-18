# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(n):
    dp = [0, 1, 2] + [0] * 1998
    if n <= 2:
        return dp[n]
    else:
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567


# import sys
#
# sys.setrecursionlimit(10000)
# dp = [-1 for _ in range(0, 2001)]
#
#
# def recursion(remain):
#     global dp
#     if remain == 0:
#         return 1
#     elif remain < 0:
#         return 0
#     else:
#         a = dp[remain - 1] if remain - 1 >= 0 and dp[remain - 1] != -1 else recursion(remain - 1)
#         b = dp[remain - 2] if remain - 2 >= 0 and dp[remain - 2] != -1 else recursion(remain - 2)
#         if dp[remain] == -1:
#             dp[remain] = (a + b) % 1234567
#         return (a + b) % 1234567
#
#
# def solution(n):
#     global dp
#     return recursion(n) % 1234567
