# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(s):
    s_list = []
    for i in range(len(s)):
        if len(s_list) != 0 and s_list[-1] == s[i]:
            del s_list[-1]
            continue
        else:
            s_list.append(s[i])
    return int(len(s_list) == 0)
