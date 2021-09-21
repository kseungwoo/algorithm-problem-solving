import itertools


def solution(orders, course):
    answer = []
    for n in course:
        d = dict()
        for o in orders:
            for k in list(itertools.combinations(o, n)):
                k = tuple(sorted(k))
                if k in d:
                    d[k] += 1
                else:
                    d[k] = 1
        for e in [k for k, v in d.items() if max(d.values()) == v and max(d.values()) > 1]:
            answer.append(''.join(e))

    return sorted(answer)
