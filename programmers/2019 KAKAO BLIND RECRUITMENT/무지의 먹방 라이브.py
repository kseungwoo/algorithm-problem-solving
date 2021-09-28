class Node:
    def __init__(self, times, index):
        self.times = times
        self.index = index
        self.next = None
        self.prev = None


def solution(food_times, k):
    fdn = len(food_times)
    if fdn == 1 and food_times[0] > k:
        return 1
    cll = [Node(fts, i) for i, fts in enumerate(food_times)]
    for i in range(len(cll)):
        if i == 0:
            cll[i].next = cll[i + 1]
            cll[i].prev = cll[len(cll) - 1]
        elif i == len(cll) - 1:
            cll[i].next = cll[0]
            cll[i].prev = cll[i - 1]
        else:
            cll[i].next = cll[i + 1]
            cll[i].prev = cll[i - 1]
    cur = cll[0]
    sorted(list(set(food_times)))
    stacked = 0
    for t in food_times:
        if (t - stacked) * fdn < k:
            k -= t * fdn
            for _ in range(fds):
                cur.times -= t - stacked
                if cur.times == 0:
                    fdn -= 1
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                cur = cur.next
            stacked += t
        else:
            break
    for _ in range(k):
        cur.times -= 1
        if cur.times == 0:
            fdn -= 1
            if fdn == 0:
                return -1
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        cur = cur.next
    answer = cur.index + 1
    return answer
