import sys

n, m = map(int, sys.stdin.readline().strip().split())

result = 0

for _ in range(n):
    data = list(map(int, sys.stdin.readline().strip().split()))
    result = max(result, min(data))

print(result)