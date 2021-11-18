# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s = "0" * (n - len(bin(arr1[i] | arr2[i])[2:])) + bin(arr1[i] | arr2[i])[2:]
        answer.append(s.replace('1', '#').replace('0', ' '))
    return answer
