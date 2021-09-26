# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def str_slice(s, n):
    sl = []
    i = 0
    while True:
        if len(s) <= i + n:
            sl.append(s[i:])
            break
        sl.append(s[i:i + n])
        i += n
    return sl


def str_merge(sl):
    ml = []
    m = ""
    for i in range(len(sl)):
        m += sl[i]
        if i + 1 < len(sl) and sl[i] == sl[i + 1]:
            continue
        else:
            ml.append(m)
            m = ""
    return ml


def str_process(ml, n):
    s = ""
    for m in ml:
        if len(m) // n >= 2:
            s += str(len(m) // n) + m[:n]
        else:
            s += m
    return len(s)


def solution(s):
    if len(s) == 1:
        return 1
    pl = []
    for n in range(1, len(s) // 2 + 1):
        sl = str_slice(s, n)
        ml = str_merge(sl)
        pl.append(str_process(ml, n))
    answer = min(pl)
    return answer
