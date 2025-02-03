def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


l = set()
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s += s[-2:]
    else:
        s += convert((n % 3) * 5, 3)
    s = int(s, 3)
    if s > 133:
        l.add(s)
print(min(l))
