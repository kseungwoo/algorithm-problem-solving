import sys

n, k = map(int, sys.stdin.readline().strip().split())
count = 0
while n > 1:
    if n % k == 0:
        count += 1
        n //= k
    else:
        count += n % k
        n -= n % k
if n == 0:
    count -= 1
print(count)
