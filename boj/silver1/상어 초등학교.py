import sys


def solution():
    N = int(sys.stdin.readline().strip())
    likes = dict()
    for _ in range(N * N):
        i1, i2, i3, i4, i5 = map(int, sys.stdin.readline().strip().split())
        likes[i1] = (i2, i3, i4, i5)
    seatMap = [[-1 for _ in range(N)] for _ in range(N)]
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
    for key, value in likes.items():
        candi_location = []
        candi_count_likes = []
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                # 비어있는 칸들에 대해
                if seatMap[r - 1][c - 1] == -1:
                    # 좋아하는 학생 수 탐색 및 저장
                    count_likes = 0
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 1 <= nr <= N and 1 <= nc <= N and seatMap[nr - 1][nc - 1] in value:
                            count_likes += 1
                    candi_location.append((r, c))
                    candi_count_likes.append(count_likes)
        # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
        if candi_count_likes.count(max(candi_count_likes)) == 1:
            r, c = candi_location[candi_count_likes.index(max(candi_count_likes))]
            # 자리 위치 저장
            seatMap[r - 1][c - 1] = key
            continue
        # 1을 만족하는 칸이 여러 개이면
        else:
            # 1을 만족하는 칸들로 candi_location 재정비
            candi_location = [v for i, v in enumerate(candi_location) if max(candi_count_likes) == candi_count_likes[i]]
            candi_count_empty = []
            # 1을 만족하는 칸들 중에서
            for r, c in candi_location:
                # 비어있는 칸들 탐색 및 저장
                count_empty = 0
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 1 <= nr <= N and 1 <= nc <= N and seatMap[nr - 1][nc - 1] == -1:
                        count_empty += 1
                candi_count_empty.append(count_empty)
            # 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
            if candi_count_empty.count(max(candi_count_empty)) == 1:
                r, c = candi_location[candi_count_empty.index(max(candi_count_empty))]
                # 자리 위치 저장
                seatMap[r - 1][c - 1] = key
                continue
            # 2를 만족하는 칸도 여러 개인 경우에는
            else:
                # 남은 칸들을 행의 번호와 열의 번호를 오름차순으로 정렬한 후
                candi_location = [v for i, v in enumerate(candi_location) if
                                  max(candi_count_empty) == candi_count_empty[i]]
                candi_location.sort(key=lambda x: (x[0], x[1]))
                # 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
                seatMap[candi_location[0][0] - 1][candi_location[0][1] - 1] = key
    # 이제 학생의 만족도를 구해야 한다. 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다.
    scoring = [0, 1, 10, 100, 1000]
    res = 0
    # 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            like = likes[seatMap[r - 1][c - 1]]
            count_likes = 0
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 1 <= nr <= N and 1 <= nc <= N and seatMap[nr - 1][nc - 1] in like:
                    count_likes += 1
            res += scoring[count_likes]
    # 학생의 만족도의 총 합
    print(res)


solution()
