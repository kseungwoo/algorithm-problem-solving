# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(n):
    if n == 1 or n == 2:
        return 1
    answer = 0
    tail, head = 1, 2
    sum_ = tail + head
    while tail <= head:
        if sum_ == n:
            answer += 1
        if sum_ <= n:
            head += 1
            sum_ += head
        else:
            sum_ -= tail
            tail += 1
    return answer
