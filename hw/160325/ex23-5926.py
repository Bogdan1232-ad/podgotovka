l = set()


def f(x, cnt, con):
    global l
    if con == 1:
        return f(x + 7, cnt + 1, 2) + f(x * 4, cnt + 1, 3)
        if cnt == 24:
            l.add(f(x + 7, cnt + 1, 2) + f(x * 4, cnt + 1, 3))
    if con == 2:
        return f(x + 1, cnt + 1, 1) + f(x * 4, cnt + 1, 3)
        if cnt == 24:
            l.add(f(x + 1, cnt + 1, 1) + f(x * 4, cnt + 1, 3))
    if con == 3:
        return f(x + 1, cnt + 1, 1) + f(x + 7, cnt + 1, 2)
        if cnt == 24:
            l.add(f(x + 1, cnt + 1, 1) + f(x + 7, cnt + 1, 2))
print(len(l))
