# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
answer = 0


def solution(numbers, target):
    def dfs(sum_, i):
        global answer
        if i == len(numbers):
            if sum_ == target:
                answer += 1
            return
        for j in range(2):
            # backup
            backup_sum_ = sum_
            # update
            if j == 0:
                sum_ += numbers[i]
            else:
                sum_ -= numbers[i]
            dfs(sum_, i + 1)
            # restore
            sum_ = backup_sum_

    dfs(0, 0)
    return answer
