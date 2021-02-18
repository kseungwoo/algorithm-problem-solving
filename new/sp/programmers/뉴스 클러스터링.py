# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def refine(s):
    s = s.upper()
    s_list = list(s)
    return ''.join(s_list)


def divide(s):
    divided_list = [s[i:i + 2] for i in range(0, len(s) - 1)]
    for i in range(len(divided_list) - 1, -1, -1):
        if not divided_list[i].isalpha():
            del divided_list[i]
    return divided_list


def make_dict(_list):
    _dict = {}
    for l in _list:
        if l in _dict.keys():
            _dict[l] += 1
        else:
            _dict[l] = 1
    return _dict


def jaccard(dict1, dict2):
    above = 0
    below = 0
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    for k in list(set(keys1) & set(keys2)):
        above += min(dict1[k], dict2[k])
    for k in list(set(keys1) | set(keys2)):
        if k in keys1 and k in keys2:
            below += max(dict1[k], dict2[k])
        elif k in keys1:
            below += dict1[k]
        else:
            below += dict2[k]

    if below == 0:
        result = 65536
    else:
        result = int((above / below) * 65536)
    return result


def solution(str1, str2):
    dict1 = make_dict(divide(refine(str1)))
    dict2 = make_dict(divide(refine(str2)))
    answer = jaccard(dict1, dict2)

    return answer
