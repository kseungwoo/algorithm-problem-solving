from itertools import combinations
import bisect


def solution(info, query):
    def lowerBound(start, end, key):
        while start < end:
            mid = (start + end) // 2
            if score_list[mid] >= key:
                end = mid
            else:
                start = mid + 1
        return end

    # Processing Info
    dict_info = {}
    split_info = []
    for _info in info:
        split_info.append(_info.split(' '))
    keys = []
    scores = []
    cases = []
    for _split_info in split_info:
        keys += ['', _split_info[0], _split_info[1], _split_info[2], _split_info[3], _split_info[0] + _split_info[1],
                 _split_info[0] + _split_info[2], _split_info[0] + _split_info[3], _split_info[1] + _split_info[2],
                 _split_info[1] + _split_info[3], _split_info[2] + _split_info[3],
                 _split_info[0] + _split_info[1] + _split_info[2], _split_info[0] + _split_info[1] + _split_info[3],
                 _split_info[0] + _split_info[2] + _split_info[3], _split_info[1] + _split_info[2] + _split_info[3],
                 _split_info[0] + _split_info[1] + _split_info[2]
                 + _split_info[3]]

        scores.append(int(_split_info[4]))
    n = 0
    for key in keys:
        key_string = ''.join(key)
        if key_string in dict_info:
            # Bad Time Complexity Occured
            # dict_info[key_string] = dict_info[key_string]+[scores[n//16]]
            dict_info[key_string].append(scores[n // 16])
        else:
            dict_info[key_string] = [scores[n // 16]]
        n += 1
    answer = []
    # Processing Query
    query_split = []
    for _query in query:
        _query = _query.replace('-', '')
        temp_split = _query.split(' and ')
        query_split.append(temp_split[:3] + temp_split[3].split(' '))
    for key in dict_info:
        dict_info[key] = sorted(dict_info[key])
    for _query_split in query_split:
        if ''.join(_query_split[:-1]) not in dict_info:
            answer.append(0)
            continue
        score_list = dict_info[''.join(_query_split[:-1])]
        dict_info[''.join(_query_split[:-1])] = score_list
        score_pass = int(_query_split[-1])
        index = bisect.bisect_left(score_list, score_pass)
        answer.append(len(score_list) - index)

    return answer
