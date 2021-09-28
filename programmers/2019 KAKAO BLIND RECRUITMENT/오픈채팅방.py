# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(record):
    d = dict()
    for r in record:
        s = r.split(' ')
        if s[0] in ['Enter', 'Change']:
            d[s[1]] = s[2]
    answer = []
    for r in record:
        s = r.split(' ')
        if s[0] == 'Enter':
            answer.append(d[s[1]] + '님이 들어왔습니다.')
        if s[0] == 'Leave':
            answer.append(d[s[1]] + '님이 나갔습니다.')
    return answer
