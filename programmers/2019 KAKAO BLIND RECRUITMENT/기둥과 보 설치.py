# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def do(build_inf, answer):
    x, y, a, b = build_inf[0], build_inf[1], build_inf[2], build_inf[3]
    # 기둥 추가
    if a == 0 and b == 1:
        if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
            answer.append([x, y, a])
    # 보 추가
    elif a == 1 and b == 1:
        if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
            answer.append([x, y, a])
    # 기둥 제거
    elif a == 0 and b == 0:
        if ([x, y + 1, 1] in answer and ([x - 1, y + 1, 1] not in answer or [x + 1, y + 1, 1] not in answer) and [x + 1, y, 0] not in answer) or ([x - 1, y + 1, 1] in answer and ([x - 2, y + 1, 1] not in answer or [x, y + 1, 1] not in answer) and [x - 1, y, 0] not in answer) or ([x, y + 1, 0] in answer and ([x - 1, y + 1, 1] not in answer and [x, y + 1, 1] not in answer)):
            return
        else:
            del answer[answer.index([x, y, a])]
    # 보 제거
    else:
        if ([x, y, 0] in answer and [x, y - 1, 0] not in answer and [x - 1, y, 1] not in answer) or ([x + 1, y, 0] in answer and [x + 1, y - 1, 0] not in answer and [x + 1, y, 1] not in answer) or ([x - 1, y, 1] in answer and ([x - 1, y - 1, 0] not in answer and [x, y - 1, 0] not in answer)) or ([x + 1, y, 1] in answer and ([x + 1, y - 1, 0] not in answer and [x + 2, y - 1, 0] not in answer)):
            return
        else:
            del answer[answer.index([x, y, a])]


def solution(n, build_frame):
    answer = []
    for build_inf in build_frame:
        do(build_inf, answer)
    answer.sort()
    return answer

# Ideal Solution 출처 : https://johnyejin.tistory.com/125
# def check(ans):
#     for x, y, what in ans:
#         if what == 0:
#             if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
#                 continue
#             else:
#                 return False
#         elif what == 1:
#             if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
#                 continue
#             else:
#                 return False
#     return True
#
#
# def solution(n, build_frame):
#     answer = []
#
#     for f in build_frame:
#         x, y, what, how = f
#
#         if how == 1:
#             answer.append([x, y, what])
#             if check(answer) is False:
#                 answer.remove([x, y, what])
#         else:
#             answer.remove([x, y, what])
#             if check(answer) is False:
#                 answer.append([x, y, what])
#
#     answer.sort()
#     return answer
