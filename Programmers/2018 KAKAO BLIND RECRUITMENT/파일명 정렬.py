from collections import defaultdict


def parse(s):
    for i, c in enumerate(s):
        if c.isdigit():
            head, rest = s[:i], s[i:]
            break
    number, tail = "", ""
    for i, c in enumerate(rest):
        if i > 4 or not (c.isdigit()):
            number, tail = rest[:i], rest[i:]
            break
    if len(number) == 0:
        number = rest
    return head, number, tail


def solution(files):
    d = defaultdict(list)
    # 문자열 파싱 후 저장
    for fn in files:
        head, number, tail = parse(fn)
        d[head.lower()].append((head, int(number), tail, fn))

    answer = []
    # HEAD 기준 정렬
    for item in sorted(d.items()):
        # NUMBER 기준 정렬
        sorted_item = sorted(item[1], key=lambda x: x[1])
        answer.extend([v[3] for v in sorted_item])
    return answer
