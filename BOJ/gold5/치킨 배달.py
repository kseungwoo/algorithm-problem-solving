from itertools import combinations
import sys


def distance(x1, y1, x2, y2):
    # 맨해튼 거리
    return abs(x1 - x2) + abs(y1 - y2)


def solution():
    # 입력 받기
    N, M = map(int, sys.stdin.readline().strip().split())
    m = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    # 도시 위치 저장
    cities = [(y, x) for y in range(N) for x in range(N) if m[y][x] == 1]
    # 치킨집 위치 저장
    chickens = [(y, x) for y in range(N) for x in range(N) if m[y][x] == 2]
    # 도시들에 대한 치킨집 위치 저장
    dl = [[distance(city[0], city[1], chicken[0], chicken[1]) for chicken in chickens] for city in cities]
    # 치킨집을 M개 선택하는 모든 경우의 수에 대해서
    # 선택한 치킨집 M개에 대해서 도시의 치킨 거리를 구하고
    # 그 중에서 최솟값을 리턴한다
    print(min(sum(min(dl[n][c] for c in cl) for n in range(len(cities))) for cl in
              list(combinations([i for i in range(len(chickens))], M))))


solution()
