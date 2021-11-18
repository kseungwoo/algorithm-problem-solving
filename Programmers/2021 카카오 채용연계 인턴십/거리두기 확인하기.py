# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
from collections import deque


def solution(places):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = []
    for n in range(len(places)):
        isFollowed = 1
        q = deque()
        for r in range(5):
            for c in range(5):
                if (places[n])[r][c] == 'P':
                    visited = [[0 for _ in range(5)] for _ in range(5)]
                    visited[r][c] = 1
                    q.append([n, r, c, 0, visited])
        while q and isFollowed == 1:
            n, r, c, move, visited = q.popleft()
            if move == 2:
                continue
            for d in range(4):
                next_r, next_c = r + dy[d], c + dx[d]
                if not (0 <= next_r < 5 and 0 <= next_c < 5):
                    continue
                if places[n][next_r][next_c] == 'P' and visited[next_r][next_c] == 0:
                    isFollowed = 0
                    break
                elif places[n][next_r][next_c] == 'X' and visited[next_r][next_c] == 0:
                    continue
                elif places[n][next_r][next_c] == 'O' and visited[next_r][next_c] == 0:
                    visited[next_r][next_c] = 1
                    q.append([n, next_r, next_c, move + 1, visited])
        answer.append(isFollowed)
    return answer
