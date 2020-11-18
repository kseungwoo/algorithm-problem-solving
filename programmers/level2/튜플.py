# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(s):
    s = s[2:-2].split('},{')
    list_s = []
    for i in s:
        list_s.append(i.split(','))
    list_s.sort(key=lambda x: len(x))
    answer = []
    for i in list_s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
                break
    return answer
