# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def rotate(o):
    l = len(o)
    t = [[0 for _ in range(l)] for _ in range(l)]
    for r in range(l):
        for c in range(l):
            t[c][r] = o[r][l - c - 1]
    return t


def solution(key, lock):
    k, l = len(key), len(lock)
    blank = set()
    filled = set()
    shape = set()
    trys = set()

    # filled and blank
    for r in range(l):
        for c in range(l):
            if lock[r][c] == 0:
                blank.add((r + k, c + k))
            else:
                filled.add((r + k, c + k))

    for _ in range(4):
        key = rotate(key)
        # shape
        for r in range(k):
            for c in range(k):
                if key[r][c] == 1:
                    shape.add((r, c))

        # try
        for r in range(0, k + l + 1):
            for c in range(0, k + l + 1):
                for s in shape:
                    trys.add((s[0] + r, s[1] + c))
                if blank & trys == blank and len(filled & trys) == 0:
                    return True
                trys.clear()
        shape.clear()

    return False