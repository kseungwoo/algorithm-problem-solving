# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenge
def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if not stack or stack[-1] == ')':
                return False
            else:
                del stack[-1]
    if stack:
        return False
    else:
        return True
