def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(1000):
    r = convert(n, 5)
    if len(r) % 2 == 0:
        r = r[len(r) // 2:] + r[:len(r) // 2]
    else:
        s = str(int(r) % 5)
        r = r + s
        r = r[len(r) // 2:] + r[:len(r) // 2]
    if r != '':
        if int(r, 5) > 50:
            print(n)
            break