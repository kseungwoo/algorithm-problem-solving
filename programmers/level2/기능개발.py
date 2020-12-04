# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(progresses, speeds):
    answer = []
    while len(progresses)!=0:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        if progresses[0]>=100:
            popped=0
            while len(progresses)!=0 and progresses[0]>=100:
                del progresses[0]
                del speeds[0]
                popped+=1
            answer.append(popped)
    return answer