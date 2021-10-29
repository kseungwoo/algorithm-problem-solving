import sys
from collections import deque
from copy import deepcopy


def fill(b, y, x, dirs, N, M):
    b = deepcopy(b)
    # 방향 - 0: 상, 1: 하, 2: 좌, 3: 우
    # dirs 방향들 에 대해 감시 받는 영역 채우기
    for d in dirs:
        if d == 0:
            for my in range(y, -1, -1):
                if b[my][x] == 6:
                    break
                b[my][x] = '#'
        elif d == 1:
            for my in range(y, N):
                if b[my][x] == 6:
                    break
                b[my][x] = '#'
        elif d == 2:
            for mx in range(x, -1, -1):
                if b[y][mx] == 6:
                    break
                b[y][mx] = '#'
        else:
            for mx in range(x, M):
                if b[y][mx] == 6:
                    break
                b[y][mx] = '#'
    return b


def solution():
    N, M = map(int, sys.stdin.readline().strip().split())
    B = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    cctv = [(y, x) for x in range(M) for y in range(N) if 1 <= B[y][x] <= 5]
    res = N * M
    # 큐 선언 및 초기화
    q = deque([(0, B)])
    # BFS
    while q:
        i, b = q.popleft()
        # 모든 cctv 체크했을 경우
        if i == len(cctv):
            # 최솟값 갱신
            res = min(res, sum(r.count(0) for r in b))
            continue
        # cctv 위치와 종류에 대한 변수
        y, x, n = cctv[i][0], cctv[i][1], B[cctv[i][0]][cctv[i][1]]
        # cctv 종류에 따라 구분하여 큐에 원소 추가
        if n == 1:
            for d in range(4):
                q.append((i + 1, fill(b, y, x, [d], N, M)))
        elif n == 2:
            q.append((i + 1, fill(b, y, x, [0, 1], N, M)))
            q.append((i + 1, fill(b, y, x, [2, 3], N, M)))
        elif n == 3:
            q.append((i + 1, fill(b, y, x, [0, 3], N, M)))
            q.append((i + 1, fill(b, y, x, [1, 3], N, M)))
            q.append((i + 1, fill(b, y, x, [1, 2], N, M)))
            q.append((i + 1, fill(b, y, x, [0, 2], N, M)))
        elif n == 4:
            q.append((i + 1, fill(b, y, x, [0, 1, 2], N, M)))
            q.append((i + 1, fill(b, y, x, [0, 1, 3], N, M)))
            q.append((i + 1, fill(b, y, x, [0, 2, 3], N, M)))
            q.append((i + 1, fill(b, y, x, [1, 2, 3], N, M)))
        else:
            q.append((i + 1, fill(b, y, x, [0, 1, 2, 3], N, M)))
    print(res)


solution()
