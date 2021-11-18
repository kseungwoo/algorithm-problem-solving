# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(n, s):
    element = s // n
    if element == 0:
        return [-1]
    answer = [element for _ in range(n)]
    index = -1
    for _ in range(s % n):
        answer[index] += 1
        index -= 1
    return answer
