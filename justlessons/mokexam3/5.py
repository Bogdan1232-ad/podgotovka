def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


l = []
for n in range(13, 14):
    r = convert(n, 4)
    if sum(map(int, r)) % 2 == 0:
        r = r + r[-2:]
    else:
        r = '2' + r + '0'
    print(r)
    if r != '':
        r = int(r, 4)
        if r % 2 == 0 and r > 120:
            l.append(r)
