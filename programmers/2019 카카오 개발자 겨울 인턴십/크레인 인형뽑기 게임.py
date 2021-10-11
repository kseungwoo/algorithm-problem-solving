def solution(board, moves):
    # stack으로 인형 쌓기
    sl = [list() for _ in range(len(board))]
    for c in range(len(board)):
        for r in range(len(board)-1,-1,-1):
            if board[r][c] == 0:
                break
            sl[c].append(board[r][c])

    bowl = list()
    count = 0
    for m in moves:
        # 인형이 집어지지 않는 경우
        if not sl[m - 1]:
            continue
        pick = sl[m - 1].pop()
        # (바구니에 인형이 있고) 같은 모양 인형 두 개 연속한 경우
        if bowl and pick == bowl[-1]:
            bowl.pop()
            count += 2
        # 연속하지 않은 경우
        else:
            bowl.append(pick)
    return count
