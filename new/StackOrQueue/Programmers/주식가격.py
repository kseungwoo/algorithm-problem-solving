# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(prices):
    answer=[]
    for i in range(len(prices)):
        notDesc=0
        for j in range(i+1,len(prices)):
            notDesc+=1
            if prices[i]>prices[j]:
                break
        answer.append(notDesc)
    return answer