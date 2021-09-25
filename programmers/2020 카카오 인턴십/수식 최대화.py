import itertools
import copy


def split_expression(expression):
    s = expression.replace('+', ' ').replace('-', ' ').replace('*', ' ')
    sl = s.split(' ')
    el = []
    for e in expression:
        if not (e.isdigit()):
            el.append(e)
    tl = []
    for i in range(len(el)):
        tl.append(sl[i])
        tl.append(el[i])
    tl.append(sl[len(sl) - 1])
    return tl


def cal(i, l):
    return i - 1, l[:i - 1] + [eval(str(l[i - 1]) + l[i] + str(l[i + 1]))] + l[i + 2:]


def solution(expression):
    tl = split_expression(expression)
    cases = list(itertools.permutations(('+', '-', '*'), 3))
    res = []
    for case in cases:
        l = copy.deepcopy(tl)
        for c in case:
            i = 0
            while True:
                if len(l) <= i:
                    break
                if l[i] == c:
                    i, l = cal(i, l)
                i += 1
        res.append(abs(l[0]))
    answer = max(res)
    return answer
