# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        seq = ''
        for a in skill_tree:
            if a in skill:
                seq += a
        if seq == skill[:len(seq)]:
            answer += 1
    return answer
