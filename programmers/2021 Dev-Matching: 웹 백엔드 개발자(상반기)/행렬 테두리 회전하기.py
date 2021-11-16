from collections import deque


def solution(rows, columns, queries):
    # 전체 보드 생성
    M = [[columns * (r - 1) + c for c in range(1, columns + 1)] for r in range(1, rows + 1)]
    result = []
    for r1, c1, r2, c2 in queries:
        q = deque()
        # 테두리를 시계 방향으로 조회하며 값 저장 (deque 이용)
        for c in range(c1, c2):
            q.append(M[r1 - 1][c - 1])
        for r in range(r1, r2):
            q.append(M[r - 1][c2 - 1])
        for c in range(c2, c1, -1):
            q.append(M[r2 - 1][c - 1])
        for r in range(r2, r1, -1):
            q.append(M[r - 1][c1 - 1])
        # 시계 방향으로 한 칸씩 밀기
        q.appendleft(q.pop())
        # 최솟값 저장
        result.append(min(q))
        # 테두리를 시계 방향으로 방문하며 값 갱신 (deque 이용)
        for c in range(c1, c2):
            M[r1 - 1][c - 1] = q.popleft()
        for r in range(r1, r2):
            M[r - 1][c2 - 1] = q.popleft()
        for c in range(c2, c1, -1):
            M[r2 - 1][c - 1] = q.popleft()
        for r in range(r2, r1, -1):
            M[r - 1][c1 - 1] = q.popleft()

    return result
