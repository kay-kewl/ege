def mysteries(st, contrary=False):
    global talks
    tmp = ''
    lst = []
    if contrary:
        st = st[::-1]
    for i in talks:
        for j in range(min(len(st), len(i))):
            if i[j] < st[j]:
                tmp += str(i[j])
            else:
                tmp += str(st[j])
        lst.append(tmp)
        tmp = ''
    talks = tuple(lst)


talks = ('wprd', 'zpu', 'fprnotes')
