def solution(lottos, win_nums):
    score_board = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    hit = 0
    for lotto in lottos:
        if lotto in win_nums:
            hit += 1
    unknown = lottos.count(0)
    min_hit = hit
    max_hit = unknown + hit
    return [score_board[max_hit], score_board[min_hit]]
