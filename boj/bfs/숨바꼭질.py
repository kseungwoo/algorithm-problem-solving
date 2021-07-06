N, K = map(int, input().split())
T = 0
visited = [0 for _ in range(100001)]
visited[N] = 1
next_move = [N]
while visited[K] == 0:
    T += 1
    temp = []
    for m in next_move:
        if m + 1 <= 100000 and visited[m + 1] == 0:
            visited[m + 1] = 1
            temp.append(m + 1)
        if m - 1 >= 0 and visited[m - 1] == 0:
            visited[m - 1] = 1
            temp.append(m - 1)
        if m * 2 <= 100000 and visited[m * 2] == 0:
            visited[m * 2] = 1
            temp.append(m * 2)
    next_move = temp
print(T)
