# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum([A[i] * B[i] for i in range(len(A))])
