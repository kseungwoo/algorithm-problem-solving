from collections import defaultdict


def solution(s):
    d = defaultdict(int)
    for n in s.replace('{', '').replace('}', '').split(','):
        d[int(n)] += 1
    return [item[0] for item in sorted(d.items(), key=lambda x: x[1], reverse=True)]
