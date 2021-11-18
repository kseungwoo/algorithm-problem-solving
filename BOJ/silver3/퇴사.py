import sys
from collections import deque


def solution():
    N = int(sys.stdin.readline().strip())
    plan = [(-1, -1)] + [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    q = deque()
    q.append((1, 0))
    # 아무 상담도 못할 경우 대비
    res = 0
    # BFS
    while q:
        day, money = q.popleft()
        res = max(res, money)
        # 다음 날이 존재할 때
        if day + 1 <= N:
            # Case 1: 당일 상담 안 할 경우
            q.append((day + 1, money))
        # 퇴사일 전까지 상담을 마칠 수 있을 때
        if day <= N and day + plan[day][0] - 1 <= N:
            # Case 2: 당일 상담을 할 경우
            q.append((plan[day][0] + day, plan[day][1] + money))
    print(res)


solution()
