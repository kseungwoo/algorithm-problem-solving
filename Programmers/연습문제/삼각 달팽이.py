# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from itertools import chain


def solution(n):
    dir_y = [1, 0, -1]
    dir_x = [0, 1, -1]
    maps = [[0 for _ in range(n)] for _ in range(n)]
    y, x = 0, 0
    index = 1
    direct = 0
    for i in range(n, 0, -1):
        for j in range(i):
            maps[y][x] = index
            index += 1
            if j == i - 1:
                direct += 1
            y += dir_y[direct % 3]
            x += dir_x[direct % 3]
    answer = [i for i in chain(*maps) if i != 0]
    return answer
