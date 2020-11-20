# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(brown, yellow):
    for n in range(1, int(yellow ** 0.5 + 1)):
        if yellow % n == 0 and (n + 2) * (yellow // n + 2) - n * (yellow // n) == brown:
            return [yellow // n + 2, n + 2]
