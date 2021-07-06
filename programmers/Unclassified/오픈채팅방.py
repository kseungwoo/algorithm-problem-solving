# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(record):
    id_name = dict()
    answer = []
    for i in range(len(record)):
        parsed = record[i].split(" ")
        if parsed[0] == "Enter":
            id_name[parsed[1]] = parsed[2]
            answer.append(parsed[1] + "님이 들어왔습니다.")
        elif parsed[0] == "Leave":
            answer.append(parsed[1] + "님이 나갔습니다.")
        else:
            id_name[parsed[1]] = parsed[2]
    for i in range(len(answer)):
        id_ = answer[i][:answer[i].find('님')]
        name_ = id_name.get(id_)
        answer[i] = answer[i].replace(id_, name_)
    return answer
