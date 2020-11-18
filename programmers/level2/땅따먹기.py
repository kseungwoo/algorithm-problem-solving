# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# By Dynamic Programming
def solution(land):
    for y in range(1, len(land)):
        for x in range(4):
            land[y][x] += max(land[y - 1][:x] + land[y - 1][x + 1:])
    return max(land[-1])


# By Dfs (Not Using DP) : Runtime Error - Too much Buffer while calculating 'score'
# max 값을 계산하기 위해 score을 저장하는 과정에서 dfs depth가 깊어지며 너무 많은 저장 값이 발생하여 버퍼가 감당하지 못하여 런타임에러가 발생하였다.
# 따라서, 중복되는 값을 memoization을 통해 DP로 풀어내는 것이 적절하였다.
"""
answer = 0
length = 0
score = 0


def dfs(index, pre, land):
    global answer
    global length
    global score
    if index == length:
        if score > answer: answer = score
        return
    for i in range(4):
        if pre == i:
            continue
        # backup
        temp_pre = pre
        temp_score = score
        # update
        pre = i
        score += land[index][i]
        dfs(index + 1, pre, land)
        # backup
        pre = temp_pre
        score = temp_score


def solution(land):
    global answer
    global length
    length = len(land)
    dfs(0, -1, land)

    return answer
"""
