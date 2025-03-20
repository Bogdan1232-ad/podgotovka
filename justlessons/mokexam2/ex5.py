def convert(num, sys):
    res = ''
    alph = '0123456789AB'
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


l = []
for n in range(10000):
    r = convert(n, 12)
    if n % 3 == 0:
        r = '1' + r + 'B'
    else:
        r = '2' + r + '0'
    r = int(r, 12)
    if r < 1966:
        l.append(r)
print(max(l))