from string import digits, ascii_uppercase

alph = digits + ascii_uppercase


def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

l = []
for n in range(1, 1000)[::-1]:
    r = convert(n, 3)
    if len(r) % 2 == 0:
        r = r[0:len(r)//2] + '0' + r[len(r)//2:]
    if int(r, 4) <= 180:
        l.append(n)
print(max(l))