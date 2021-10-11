from itertools import product


def check(s, _id):
    if len(s) != len(_id):
        return False
    for i in range(len(s)):
        if not (s[i] == _id[i] or _id[i] == '*'):
            return False
    return True


def search(_id, _list):
    sl = list()
    for s in _list:
        if check(s, _id):
            sl.append(s)
    return sl


def solution(user_id, banned_id):
    sll = [search(_id, user_id) for _id in banned_id]
    ans = set()
    for candi in product(*sll):
        if len(set(candi)) == len(banned_id):
            ans.add(''.join(sorted(candi)))
    return len(ans)

#
# from itertools import product
#
#
# def search(k, _list):
#     sl = list()
#     for s in _list:
#         if len(s) != len(k):
#             continue
#         isCorrect = True
#         for i in range(len(s)):
#             if not (s[i] == k[i] or k[i] == '*'):
#                 isCorrect = False
#                 break
#         if isCorrect:
#             sl.append(s)
#     return sl
#
#
# def solution(user_id, banned_id):
#     sll = list()
#     answer = set()
#     for _id in banned_id:
#         sll.append(search(_id, user_id))
#     for candi in product(*sll):
#         if len(set(candi)) == len(banned_id):
#             answer.add(''.join(sorted(candi)))
#     return len(answer)
