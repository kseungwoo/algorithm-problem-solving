# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def distance(l1, l2):
    loc = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2),
           '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    x1, y1, x2, y2 = loc[l1][0], loc[l1][1], loc[l2][0], loc[l2][1]
    return abs(x1 - x2) + abs(y1 - y2)


def solution(numbers, hand):
    ll, rl, hand = '*', '#', hand[0].upper()
    answer = ''
    for n in numbers:
        if n in (1, 4, 7):
            answer += 'L'
            ll = n
        elif n in (3, 6, 9):
            answer += 'R'
            rl = n
        else:
            if distance(ll, n) == distance(rl, n):
                answer += hand
                if hand == 'R':
                    rl = n
                else:
                    ll = n
            elif distance(ll, n) < distance(rl, n):
                answer += 'L'
                ll = n
            else:
                answer += 'R'
                rl = n
    return answer
