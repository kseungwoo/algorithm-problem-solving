# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from collections import deque

def solution(priorities, location):
    priorities=deque(priorities)
    nth = 0
    sequences = deque(i for i in range(len(priorities)))
    while True:
        nth += 1
        priority = priorities.popleft()
        sequence = sequences.popleft()
        for p in priorities:
            if p > priority:
                priorities.append(priority)
                sequences.append(sequence)
                break
        if len(sequences) != 0 and sequence == sequences[-1]:
            nth -= 1
        elif sequence == location:
            return nth

# def solution(priorities, location):
#     nth = 0
#     sequences = [i for i in range(len(priorities))]
#     while True:
#         nth += 1
#         priority = priorities.pop(0)
#         sequence = sequences.pop(0)
#         for p in priorities:
#             if p > priority:
#                 priorities.append(priority)
#                 sequences.append(sequence)
#                 break
#         if len(sequences) != 0 and sequence == sequences[-1]:
#             nth -= 1
#         elif sequence == location:
#             return nth




# def solution(priorities, location):
#     curPoint = 0
#     reqPoint = location
#     printPoint = curPoint
#     _time = 0
#     while priorities:
#         _time += 1
#         maxPriority = 0
#
#         for _ in range(len(priorities)):
#             if priorities[curPoint] > maxPriority:
#                 printPoint = curPoint
#                 maxPriority = priorities[curPoint]
#             curPoint = (curPoint + 1) % len(priorities)
#
#         if reqPoint == printPoint:
#             break
#         elif reqPoint > printPoint:
#             reqPoint -= 1
#
#         del priorities[printPoint]
#         curPoint = printPoint % len(priorities)
#
#     answer = _time
#     return _time