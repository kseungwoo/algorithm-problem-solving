from collections import defaultdict
import heapq


def solution(stones, k):
    hq = [-stones[i] for i in range(0, k)]
    heapq.heapify(hq)
    dt = defaultdict(int)
    for i in range(0, k):
        dt[stones[i]] += 1
    answers = [-hq[0]]
    # 투 포인터(Two Pointers) 선언
    start, end = 1, k
    while end < len(stones):
        # 삭제
        dt[stones[start - 1]] -= 1
        # 삽입
        dt[stones[end]] += 1
        heapq.heappush(hq, -stones[end])
        # 조회 후 비교 (Greedy)
        while dt[-hq[0]] == 0:
            heapq.heappop(hq)
        answers.append(-hq[0])
        start, end = start + 1, end + 1
    return min(answers)