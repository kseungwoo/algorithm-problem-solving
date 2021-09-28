def content(page):
    return page.split('<head>')[1].split('</head>')[0].split('<meta property="og:url" content="')[1].split('"/>')[0]


def exlink(page):
    body = page.split('<body>')[1].split('</body>')[0]
    sp1 = body.split('<a href=')
    sp2 = []
    res = []
    for s in sp1:
        sp2.extend(s.split('>'))
    for s in sp2:
        if s[0] == '"' and s[-1] == '"':
            res.append(s[1:-1])
    return tuple(res)


def cntword(page, word):
    count = 0
    while page.find(word) != -1:
        if not (page[page.find(word) - 1].isalpha() or page[page.find(word) + len(word)].isalpha()):
            count += 1
        page = 'a' + page[page.find(word) + len(word):]
        print(page)
    return count


def solution(word, pages):
    d = dict()
    for page in pages:
        d[content(page)] = [cntword(page.lower(), word.lower()), len(exlink(page)), 0]
    for page in pages:
        for l in exlink(page):
            if d.get(l) is None:
                continue
            else:
                d[l][2] += d[content(page)][0] / d[content(page)][1]
    scores = []
    for key in d.keys():
        scores.append(d[key][0] + d[key][2])

    return scores.index(max(scores))
