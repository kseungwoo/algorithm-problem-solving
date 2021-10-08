def rev(N, n):
    d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
         13: 'D', 14: 'E', 15: 'F'}
    s = ''
    if N == 0:
        return '0'
    while N > 0:
        N, mod = divmod(N, n)
        s += d[mod]
    return s[::-1]


def solution(n, t, m, p):
    s, N = "", 0
    while len(s) < m * t:
        s += rev(N, n)
        N += 1
    result, turn = "", p - 1
    for _ in range(t):
        result += s[turn]
        turn += m
    return result
