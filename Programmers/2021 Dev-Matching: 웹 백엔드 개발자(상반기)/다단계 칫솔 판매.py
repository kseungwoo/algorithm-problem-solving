from collections import defaultdict


def divide_revenue(revenue, seller, recommend, amount):
    yours = amount // 10
    mine = amount - yours
    revenue[seller] += mine
    if yours > 0 and recommend[seller] != '-':
        divide_revenue(revenue, recommend[seller], recommend, yours)


def solution(enroll, referral, seller, amount):
    recommend = dict()
    for i in range(len(enroll)):
        recommend[enroll[i]] = referral[i]
    revenue = defaultdict(int)
    for i, sr in enumerate(seller):
        divide_revenue(revenue, sr, recommend, amount[i] * 100)
    return [revenue[e] for e in enroll]
