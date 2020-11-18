# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 분할 정복 (Divide And Conquer) - In fact, Conquer and Divide.
# !=Divide and Check, == Check and Divide
import itertools

result_zero, result_one = 0, 0


def check(arr, r, c, n):
    count = 0
    for y in range(r, r + n):
        for x in range(c, c + n):
            count += arr[y][x]
    return 1 if count == n ** 2 else 0 if count == 0 else -1


def quad_tree(arr, r, c, n):
    global result_zero
    global result_one
    if n == 1: return
    if check(arr, r, c, n) >= 0:
        if check(arr, r, c, n) == 1:
            result_one -= n ** 2 - 1
        else:
            result_zero -= n ** 2 - 1
    else:
        n = n // 2
        quad_tree(arr, r, c, n)
        quad_tree(arr, r + n, c, n)
        quad_tree(arr, r, c + n, n)
        quad_tree(arr, r + n, c + n, n)


def solution(arr):
    global result_zero
    global result_one

    result_one = sum(itertools.chain(*arr))
    result_zero = len(arr) ** 2 - result_one

    quad_tree(arr, 0, 0, len(arr))
    answer = [result_zero, result_one]
    return answer

# result_zero,result_one=0,0

# def check(arr,r,c,n):
#     zero,one=0,0
#     for y in range(r,r+n):
#         for x in range(c,c+n):
#             if arr[y][x]==0:
#                 zero=1
#             else:
#                 one=1
#     if zero==one:
#         return -1
#     elif zero==1:
#         return 0
#     else:
#         return 1


# def quad_tree(arr,r,c,n):
#     global result_zero
#     global result_one
#     if n==1: return
#     n=n//2
#     print(n)
# #     1
#     if check(arr,r,c,n)>=0:
#         if check(arr,r,c,n)==1:
#             result_one-=n**2-1
#         else:
#             result_zero-=n**2-1
#     else:
#         quad_tree(arr,r,c,n)
# #         2
#     if check(arr,r+n,c,n)>=0:
#         if check(arr,r+n,c,n)==1:
#             result_one-=n**2-1
#         else:
#             result_zero-=n**2-1
#     else:
#         quad_tree(arr,r+n,c,n)
# #     3
#     if check(arr,r,c+n,n)>=0:
#         if check(arr,r,c+n,n)==1:
#             result_one-=n**2-1
#         else:
#             result_zero-=n**2-1
#     else:
#         quad_tree(arr,r,c+n,n)
# #     4
#     if check(arr,r+n,c+n,n)>=0:
#         if check(arr,r+n,c+n,n)==1:
#             result_one-=n**2-1
#         else:
#             result_zero-=n**2-1
#     else:
#         quad_tree(arr,r+n,c+n,n)


# def solution(arr):
#     global result_zero
#     global result_one


#     for i in arr:
#         for j in i:
#             if j==0:
#                 result_zero+=1
#             else:
#                 result_one+=1

#     quad_tree(arr,0,0,len(arr))
#     answer=[result_zero,result_one]
#     return answer
