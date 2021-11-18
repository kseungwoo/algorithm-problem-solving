# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(n):
    dp = [0, 1, 2] + [0] * 1998
    if n <= 2:
        return dp[n]
    else:
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567
