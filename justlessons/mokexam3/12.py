for s in range(4, 10000):
    r = '1' + '2' * s
    while '12' in r or '32' in r or '22' in r:
        r = r.replace('12', '22', 1)
        r = r.replace('32', '211', 1)
        r = r.replace('22', '3', 1)
    if sum(map(int, r)) % 6 == 0:
        print(s)
        break
