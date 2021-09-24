def toSecond(s):
    s = s.split(':')
    return int(s[0]) * 3600 + int(s[1]) * 60 + int(s[2])


def solution(play_time, adv_time, logs):
    total = toSecond(play_time)
    tl = [0 for _ in range(total + 1)]
    for log in logs:
        start, end = toSecond(log.split('-')[0]), toSecond(log.split('-')[1])
        tl[start] += 1
        tl[end] -= 1
    sl = []
    n = 0
    for e in tl:
        n += e
        sl.append(n)

    adlen = toSecond(adv_time)
    start, end, maxv, curv, maxt = 1, adlen, sum(sl[:adlen]), sum(sl[:adlen]), 0
    while end < total:
        curv = curv - sl[start - 1] + sl[end]
        if maxv < curv:
            maxv = curv
            maxt = start
        start += 1
        end += 1

    answer = ''

    if len(str(maxt // 3600)) == 1:
        answer += '0'
    answer += str(maxt // 3600) + ':'
    if len(str((maxt % 3600) // 60)) == 1:
        answer += '0'
    answer += str((maxt % 3600) // 60) + ':'
    if len(str((maxt % 60))) == 1:
        answer += '0'
    answer += str((maxt % 60))

    return answer
