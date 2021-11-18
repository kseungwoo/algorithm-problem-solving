# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
import heapq


def solution(scoville, K):
    blend_n = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        blend_n += 1
    if scoville[0] >= K:
        return blend_n
    else:
        return -1
