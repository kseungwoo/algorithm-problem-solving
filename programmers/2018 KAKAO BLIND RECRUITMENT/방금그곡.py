def parse(m):
    p = list()
    for i in range(len(m)):
        if m[i] == '#':
            continue
        elif i != len(m) - 1 and m[i + 1] == '#':
            p.append(m[i:i + 2] + '-')
        else:
            p.append(m[i] + '-')
    return p


def solution(m, musicinfos):
    # musicinfos 전처리
    plays = list()
    for info in musicinfos:
        sl = info.split(',')
        pl = parse(sl[3])
        length = (int(sl[1].split(':')[0]) * 60 + int(sl[1].split(':')[1]))-(int(sl[0].split(':')[0]) * 60 + int(sl[0].split(':')[1]))
        play = pl * (length // len(pl)) + pl[:(length % len(pl))]
        plays.append((sl[2], ''.join(play), length))
    # 방금그곡 후보 검색
    candi = []
    for play in plays:
        if ''.join(parse(m)) in play[1]:
            candi.append(play)
    # 방금그곡 최종 선정
    if len(candi) == 0:
        return '(None)'
    candi.sort(key=lambda x: x[2], reverse=True)
    return candi[0][0]
