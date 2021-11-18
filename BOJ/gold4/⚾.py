import sys
from itertools import permutations


def game(players, seq, N):
    score = 0
    i = 0
    for n in range(N):
        b1, b2, b3 = 0, 0, 0
        out = 0
        while out < 3:
            if players[n][seq[i]] == 0:
                out += 1
            elif players[n][seq[i]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif players[n][seq[i]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif players[n][seq[i]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif players[n][seq[i]] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            i = i + 1 if i + 1 < 9 else 0

    return score


def solution():
    N = int(sys.stdin.readline().strip())
    players = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    print(max(game(players, list(p)[:3] + [0] + list(p)[3:], N) for p in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8)))


solution()
