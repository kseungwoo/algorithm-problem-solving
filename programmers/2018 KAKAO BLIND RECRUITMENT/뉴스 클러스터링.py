from collections import defaultdict


def parse_and_store(_str):
    _set = set()
    _dic = defaultdict(int)
    for i in range(len(_str) - 1):
        s = _str[i:i + 2]
        if s.isalpha():
            _set.add(s.lower())
            _dic[s.lower()] += 1
    return _set, _dic


def solution(str1, str2):
    set1, dic1 = parse_and_store(str1)
    set2, dic2 = parse_and_store(str2)
    if len(set1) == len(set2) == 0:
        jac = 1
    else:
        jac = sum(min(dic1[s], dic2[s]) for s in (set1 & set2)) / sum(max(dic1[s], dic2[s]) for s in (set1 | set2))
    return int(jac * 65536)
