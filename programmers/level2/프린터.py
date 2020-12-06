# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(priorities, location):
    nth = 0
    sequences = [i for i in range(len(priorities))]
    while True:
        nth += 1
        priority = priorities[0]
        sequence = sequences[0]
        del priorities[0]
        del sequences[0]
        for p in priorities:
            if p > priority:
                priorities.append(priority)
                sequences.append(sequence)
                break
        if len(sequences) != 0 and sequence == sequences[-1]:
            nth -= 1
        elif sequence == location:
            return nth
