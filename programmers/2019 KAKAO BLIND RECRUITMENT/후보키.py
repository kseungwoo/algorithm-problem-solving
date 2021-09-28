from itertools import combinations


def solution(relation):
    r = len(relation)
    c = len(relation[0])
    cl = [i for i in range(c)]
    unq = []
    for n in range(1, c + 1):
        for ch in tuple(combinations(cl, n)):
            tmp = [tuple(rel[j] for j in ch) for rel in relation]
            if len(set(tmp)) == r:
                unq.append(ch)
    ex = set()
    for i in range(len(unq) - 1):
        for j in range(i + 1, len(unq)):
            if set(unq[i]) & set(unq[j]) == set(unq[i]):
                ex.add(unq[j])
    answer = len(unq) - len(ex)
    return answer