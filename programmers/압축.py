# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(msg):
    dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
            "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
            "Z": 26}
    answer = []
    dict_i = 27
    while len(msg) > 0:
        index = len(msg)
        while dict.get(msg[:index]) is None:
            index -= 1
        answer.append(dict.get(msg[:index]))
        if index != len(msg):
            dict[msg[:index + 1]] = dict_i
            dict_i += 1
        msg = msg[index:]
    return answer
