# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def isRight(p):
    l = []
    for s in p:
        if s == '(':
            l.append('(')
        else:
            if len(l) > 0:
                l.pop()
            else:
                return False
    if len(l) == 0:
        return True
    else:
        return False


def reverse(s):
    r = ""
    for c in s:
        if c == '(':
            r += ')'
        else:
            r += '('
    return r


def recursion(p):
    # Step 1
    if len(p) == 0:
        return ""
    # Step 2
    for i in range(0, len(p)):
        if i == len(p) - 1:
            u, v = p[:], ""
            break
        if p[:i + 1].count('(') == p[:i + 1].count(')') and p[:i + 1].count('(') != 0:
            u, v = p[:i + 1], p[i + 1:]
            break
    # Step 3
    if isRight(u):
        return u + recursion(v)
    # Step 4
    return '(' + recursion(v) + ')' + reverse(u[1:-1])


def solution(p):
    # isRight
    if isRight(p):
        return p
    return recursion(p)
