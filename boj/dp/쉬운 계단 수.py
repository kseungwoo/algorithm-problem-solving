import copy

N = int(input())
digit = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(2, N + 1):
    ans_new = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        if i == 0:
            ans_new[1] = (ans_new[1] + digit[0]) % 1000000000

        elif i == 9:
            ans_new[8] = (ans_new[8] + digit[9]) % 1000000000
        else:
            ans_new[i + 1] = (ans_new[i+1] + digit[i]) % 1000000000
            ans_new[i - 1] = (ans_new[i-1] + digit[i]) % 1000000000
    digit = copy.deepcopy(ans_new)

print(sum(digit)% 1000000000)
