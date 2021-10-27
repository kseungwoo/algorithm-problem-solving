import sys


def play(N, K, board, pm, pl, turns):
    # 4가지 방향 변수
    dy, dx = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0)
    # 방향 전환 변수
    change = {1: 2, 2: 1, 3: 4, 4: 3}
    for i in range(K):
        # y좌표, x좌표, 스택에서 말의 위치
        y, x, s = pl[i]
        ny, nx = y + dy[turns[i]], x + dx[turns[i]]
        # 이동하는 칸이 흰색일 경우
        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
            pm[ny][nx] += pm[y][x][s:]
            for p in pm[y][x][s:]:
                pl[p] = ny, nx, pm[ny][nx].index(p)
            pm[y][x] = pm[y][x][:s]
        # 이동하는 칸이 빨간색일 경우
        elif 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 1:
            pm[ny][nx] += pm[y][x][s:][::-1]
            for p in pm[y][x][s:]:
                pl[p] = ny, nx, pm[ny][nx].index(p)
            pm[y][x] = pm[y][x][:s]
        # 이동하는 칸이 파란색이거나 체스판을 벗어나는 경우
        else:
            # 방향 전환
            turns[i] = change[turns[i]]
            # 다시 한 칸 이동
            ny, nx = y + dy[turns[i]], x + dx[turns[i]]
            # 이동하는 칸이 흰색일 경우
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                pm[ny][nx] += pm[y][x][s:]
                for p in pm[y][x][s:]:
                    pl[p] = ny, nx, pm[ny][nx].index(p)
                pm[y][x] = pm[y][x][:s]
            # 이동하는 칸이 빨간색일 경우
            elif 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 1:
                pm[ny][nx] += pm[y][x][s:][::-1]
                for p in pm[y][x][s:]:
                    pl[p] = ny, nx, pm[ny][nx].index(p)
                pm[y][x] = pm[y][x][:s]
            # 이동하는 칸이 파란색이거나 체스판을 벗어나는 경우
            else:
                continue
        # 4개 이상 쌓이는 순간 게임이 종료된다
        if len(pm[ny][nx]) >= 4:
            return False
    # 게임을 계속 진행한다
    return True


def solution():
    # N, K 입력 받기
    N, K = map(int, sys.stdin.readline().strip().split())
    # 체스판의 색깔 정보 입력 받기
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    # Player Map: 체스판의 좌표로부터 플레이어의 정보를 조회한다
    pm = [[list() for _ in range(N)] for _ in range(N)]
    # Player Location: 플레이어의 정보로부터 체스판에서의 위치를 조회한다.
    pl = list()
    # Turns: 각 플레이어의 턴마다 이동하는 방향을 조회한다.
    turns = list()
    for i in range(K):
        # 플레이어의 위치 좌표 y, x와 이동 방향 정보를 받는다.
        y, x, t = map(int, sys.stdin.readline().strip().split())
        # 플레이어의 정보 추가
        pm[y - 1][x - 1].append(i)
        pl.append((y - 1, x - 1, len(pm[y - 1][x - 1]) - 1))
        turns.append(t)
    result = 1
    # False를 반환하거나 result가 1000을 초과할 때까지 play를 호출한다
    while play(N, K, board, pm, pl, turns):
        if result > 1000:
            print(-1)
            exit(0)
        result += 1
    print(result)


solution()
