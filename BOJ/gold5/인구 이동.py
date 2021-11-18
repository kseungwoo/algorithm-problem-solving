import sys
from collections import deque


def bfs(y, x, checked, m, N, L, R):
    # 연합을 이루고 있는 나라들 위치 저장
    u = [(y, x)]
    # BFS
    q = deque()
    q.append((y, x))
    checked[y][x] = 1
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and checked[ny][nx] == 0 and L <= abs(m[ny][nx] - m[y][x]) <= R:
                checked[ny][nx] = 1
                q.append((ny, nx))
                u.append((ny, nx))
    # 연합된 나라들에 대한 인구 이동 실시
    p = sum(m[y][x] for y, x in u) // len(u)
    for y, x in u:
        m[y][x] = p


def move(m, N, L, R):
    # 중복 체크를 막기 위한 자료구조
    checked = [[0 for _ in range(N)] for _ in range(N)]
    # 체크 횟수 카운트
    cnt = 0
    # 이중 for문
    for y in range(N):
        for x in range(N):
            # 만약 아직 체크되지 않았다면
            if checked[y][x] == 0:
                # 체크 횟수 + 1
                cnt += 1
                # 해당 좌표에 대해 bfs
                bfs(y, x, checked, m, N, L, R)
    # 만약 인구 이동이 없었다면
    if cnt == N * N:
        return False
    # 인구 이동이 있었다면
    else:
        return True


def solution():
    N, L, R = map(int, sys.stdin.readline().strip().split())
    m = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    res = 0
    # 인구 이동이 더이상 발생하지 않을 때까지 move 반복 호출
    while move(m, N, L, R):
        res += 1
    print(res)


solution()
