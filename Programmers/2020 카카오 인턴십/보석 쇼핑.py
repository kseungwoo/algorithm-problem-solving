# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(gems):
    ri = []
    rl = []
    total = len(set(gems))
    sel = dict({gems[0]: 1})
    start = end = 0
    while True:
        if len(sel) == total:
            ri.append([start + 1, end + 1])
            rl.append(end - start)
            sel[gems[start]] -= 1
            if sel[gems[start]] == 0:
                del sel[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if sel.get(gems[end]) is None:
                sel[gems[end]] = 1
            else:
                sel[gems[end]] += 1

    answer = []
    minrl = min(rl)
    for i in range(len(ri)):
        if rl[i] == minrl:
            answer = ri[i]
            break
    return answer
