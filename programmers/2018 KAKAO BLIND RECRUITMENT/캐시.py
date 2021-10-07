from collections import deque


def solution(cacheSize, cities):
    dq = deque(maxlen=cacheSize)
    t = 0
    for city in cities:
        s = city.lower()
        if s in dq:
            t += 1
            dq.remove(s)
        else:
            t += 5
        dq.append(s)
    return t
