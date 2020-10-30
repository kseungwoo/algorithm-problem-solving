# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(phone_book):
    dict = {}
    for phone_number in phone_book:
        dict[phone_number] = 1
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if dict.get(phone_number[:i]) is not None:
                return False
    return True
