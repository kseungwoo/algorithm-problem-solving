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
