# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def check(n, m):
    str_n = format(n, 'b')
    str_next = format(m, 'b')
    if sum(list(map(int, str_n))) == sum(list(map(int, str_next))):
        return True
    else:
        return False


def solution(n):
    ans = n + 1
    while not check(n, ans):
        ans += 1
    return ans
