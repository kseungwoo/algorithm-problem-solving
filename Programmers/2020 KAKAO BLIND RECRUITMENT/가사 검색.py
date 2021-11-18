from bisect import bisect_right, bisect_left
from collections import defaultdict


def search_words(query, lst):
    return bisect_right(lst, query.replace('?', 'z')) - bisect_left(lst, query.replace('?', 'a'))


def solution(words, queries):
    res = []
    fwd = defaultdict(list)
    rvs = defaultdict(list)

    for word in words:
        fwd[len(word)].append(word)
        rvs[len(word)].append(word[::-1])

    for value in fwd.values():
        value.sort()
    for value in rvs.values():
        value.sort()

    for query in queries:
        if query[0] == '?':
            res.append(search_words(query[::-1], rvs[len(query)]))
        else:
            res.append(search_words(query, fwd[len(query)]))

    return res
