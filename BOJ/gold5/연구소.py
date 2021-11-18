import sys
from collections import deque
from itertools import combinations
import copy


def spread(b, q, case, N, M):
    # 깊은 복사
    b, q = copy.deepcopy(b), copy.deepcopy(q)
    # 벽으로 채우기
    for y, x in case:
        b[y][x] = 1
    # 4가지 방향 변수 선언
    dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
    # BFS
    while q:
        y, x = q.popleft()
        # 4가지 방향에 대해 빈 칸이면 바이러스 전파
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and b[ny][nx] == 0:
                b[ny][nx] = 2
                q.append((ny, nx))
    # 빈칸의 개수 리턴
    return sum(row.count(0) for row in b)


def solution():
    # N, M 입력
    N, M = map(int, sys.stdin.readline().strip().split())
    # 전체 맵 입력
    b = list()
    for _ in range(N):
        b.append(list(map(int, sys.stdin.readline().strip().split())))
    # 바이러스 처음 위치 큐에 저장
    q = deque((y, x) for y in range(N) for x in range(M) if b[y][x] == 2)
    # 빈 칸 중 3개를 선택하는 모든 경우의 수
    cases = list(combinations([(y, x) for y in range(N) for x in range(M) if b[y][x] == 0], 3))
    # 모든 경우에 대해 바이러스 퍼트려보고 그 중 안전 지역 최댓값 출력
    print(max(spread(b, q, case, N, M) for case in cases))


solution()
