# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

NOTE = '0123456789ABCDEF'
def change(num, base):
    q, r = divmod(num, base)
    n = NOTE[r]
    return change(q, base) + n if q else n


def solution(n, t, m, p):
    candi = ''
    candi_max_len = m * (t - 1) + p
    candi_i = 0
    while len(candi) < candi_max_len:
        candi += str(change(candi_i, n))
        candi_i += 1
    candi = candi[:candi_max_len]

    answer = ''
    answer_i = p - 1

    while answer_i < candi_max_len:
        answer += candi[answer_i]
        answer_i += m
    return answer
