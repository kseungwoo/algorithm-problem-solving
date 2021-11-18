# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
answer_list = []


def dfs(route, tickets, departure):
    global answer_list
    if len(tickets) == 0:
        answer_list.append(route)
        return
    for i in range(len(tickets)):
        if tickets[i][0] == departure:
            dfs(route + [tickets[i][1]], tickets[:i] + tickets[i + 1:], tickets[i][1])


def solution(tickets):
    global answer_list
    dfs(["ICN"], tickets, "ICN")
    answer_list.sort()
    return answer_list[0]

# Failed With Greedy Algorithm
# ----------------------------
# def solution(tickets):
#     answer = ["ICN"]
#     departure="ICN"
#     while len(tickets)>=1:
#         candi=[]
#         for i in range(len(tickets)-1,-1,-1):
#             if tickets[i][0]==departure:
#                 candi.append(tickets[i][1])
#                 del tickets[i]
#         candi.sort()
#         answer.append(candi[0])
#         if len(candi)>1:
#             for i in range(len(candi)-1,0,-1):
#                 tickets.append([departure,candi[i]])
#         departure=candi[0]
#     return answer
