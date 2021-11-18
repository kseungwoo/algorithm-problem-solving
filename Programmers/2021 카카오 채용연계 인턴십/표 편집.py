# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

class Node:
    def __init__(self):
        self.removed = False
        self.next = None
        self.prev = None


def solution(n, k, cmd):
    dl = [Node() for _ in range(n)]
    for i in range(len(dl)):
        if i == 0:
            dl[i].next = dl[i + 1]
        elif i == n - 1:
            dl[i].prev = dl[i - 1]
        else:
            dl[i].prev = dl[i - 1]
            dl[i].next = dl[i + 1]
    cur = dl[k]
    bk = list()
    for i in range(len(cmd)):
        if cmd[i][0] == 'U':
            for _ in range(int(cmd[i][2:])):
                cur = cur.prev
        elif cmd[i][0] == 'D':
            for _ in range(int(cmd[i][2:])):
                cur = cur.next
        elif cmd[i][0] == 'C':
            bk.append(cur)
            cur.removed = True
            # Case 1 : 마지막 노드
            if cur.next == None:
                cur.prev.next = None
                cur = cur.prev
            # Case 2 : 첫 노드
            elif cur.prev == None:
                cur.next.prev = None
                cur = cur.next
            # Case 3 : 증간 노드
            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = cur.next
        else:
            bk_n = bk.pop()
            bk_n.removed = False
            # Case 1 : 마지막 노드
            if bk_n.next == None:
                bk_n.prev.next = bk_n
            # Case 2 : 첫 노드
            elif bk_n.prev == None:
                bk_n.next.prev = bk_n
            # Case 3 : 증간 노드
            else:
                bk_n.prev.next = bk_n
                bk_n.next.prev = bk_n

    answer = ''
    for i in range(len(dl)):
        if dl[i].removed == False:
            answer = answer + 'O'
        else:
            answer = answer + 'X'

    return answer
