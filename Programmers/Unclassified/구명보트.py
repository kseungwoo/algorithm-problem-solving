# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from collections import deque


def solution(people, limit):
    boat_n = 0
    people.sort()
    people = deque(people)
    boat_n += 1
    first = people.popleft()
    while people:
        if first + people.pop() <= limit:
            if people:
                first = people.popleft()
                boat_n += 1
            else:
                return boat_n
        else:
            boat_n += 1
    return boat_n
