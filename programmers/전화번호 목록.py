# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

def solution(phone_book):
    dict = {}
    for phone_number in phone_book:
        dict[phone_number] = 1
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if dict.get(phone_number[:i]) is not None:
                return False
    return True
