import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))

data.sort(reverse=True)
ans = 0
n1, n2 = data[0], data[1]
while True:
    for _ in range(k):
        if m > 0:
            m -= 1
            ans += n1
        else:
            print(ans)
            exit(0)
    if m > 0:
        m -= 1
        ans += n2
    else:
        print(ans)
        exit(0)
