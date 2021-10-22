def solution(land):
    for y in range(1, len(land)):
        for x in range(4):
            land[y][x] += max(land[y - 1][:x] + land[y - 1][x + 1:])
    return max(land[-1])
