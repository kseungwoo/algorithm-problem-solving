# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(n):
    pibo = [0, 1, 1]
    if 0 <= n <= 2:
        return pibo[n]
    for i in range(3, n + 1):
        pibo.append((pibo[i - 1] + pibo[i - 2]) % 1234567)
    return pibo[n]
