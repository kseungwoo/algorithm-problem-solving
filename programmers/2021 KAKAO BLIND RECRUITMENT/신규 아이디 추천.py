# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(new_id):
    # Step 1
    id1 = new_id.lower()
    # Step 2
    id2 = ""
    for c in id1:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            id2 = id2 + c
    # Step 3
    dotBefore = False
    id3 = ""
    for c in id2:
        if c != '.':
            dotBefore = False
            id3 = id3 + c
        elif c == '.':
            if not dotBefore:
                dotBefore = True
                id3 = id3 + c
    # Step 4
    id4 = id3
    if id4 == "." or id4 == "..":
        id4 = ""
    else:
        if id4[0] == '.':
            id4 = id4[1:]
        if id4[-1] == '.':
            id4 = id4[:-1]
    # Step 5
    id5 = id4
    if id5 == "":
        id5 += "a"
    # Step 6
    id6 = id5
    if len(id6) >= 16:
        id6 = id6[:15]
        if id6[-1] == '.':
            id6 = id6[:-1]
    # Step 7
    id7 = id6
    if len(id7) <= 2:
        while len(id7) != 3:
            id7 = id7 + id7[-1]

    answer = id7
    return answer
