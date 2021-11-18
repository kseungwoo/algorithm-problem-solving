def zipping(msg, d, answer):
    for i in range(len(msg), 0, -1):
        if d.get(msg[:i]):
            answer.append(d[msg[:i]])
            if len(msg[i:]) != 0:
                d[msg[:i + 1]] = len(d) + 1
            return msg[i:]


def solution(msg):
    answer = []
    d = dict()
    for a in range(65, 91):
        d[chr(a)] = a - 64
    while len(msg) != 0:
        msg = zipping(msg, d, answer)
    return answer
