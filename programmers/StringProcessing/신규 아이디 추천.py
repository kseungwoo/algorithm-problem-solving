# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(new_id):
    _id = new_id
    # 1
    _id = _id.lower()
    # 2
    for i in range(len(_id) - 1, -1, -1):
        if not _id[i].isalpha() and not _id[i].isdigit() and _id[i] != '.' and _id[i] != '-' and _id[i] != '_':
            _id = _id[:i] + _id[i + 1:]
    # 3
    for n in range(len(_id) - 1, 1, -1):
        _id = _id.replace('.' * n, '.')
    # 4
    if len(_id) != 0 and _id[0] == '.':
        if len(_id) == 1:
            _id = ''
        else:
            _id = _id[1:]
    if len(_id) != 0 and _id[-1] == '.':
        if len(_id) == 1:
            _id = ''
        else:
            _id = _id[:len(_id) - 1]
    # 5
    if len(_id) == 0:
        _id = 'a'
    # 6
    if len(_id) >= 16:
        _id = _id[:15]
        if _id[-1] == '.':
            _id = _id[:len(_id) - 1]
    # 7
    if len(_id) <= 2:
        while len(_id) != 3:
            _id = _id + _id[-1]
    return _id
