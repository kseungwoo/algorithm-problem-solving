# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(s):
    voca_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for index in range(10):
        s = s.replace(voca_list[index], num_list[index])
    return int(s)