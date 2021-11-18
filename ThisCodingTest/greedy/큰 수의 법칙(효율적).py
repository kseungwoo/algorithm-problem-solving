import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))

data.sort(reverse=True)
first, second = data[0], data[1]
count = int(m / (k + 1)) * k + m % (k + 1)
result = count * first + (m - count) * second
print(result)
