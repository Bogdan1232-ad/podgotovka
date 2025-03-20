def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(1, 1000):
    s = convert(n, 3)
    if sum(map(int, s)) % 2 == 0:
        s = '12' + s[2:] + '0'
    else:
        s = '10' + s[2:] + '2'
    if int(s, 3) > 105:
        print(n)
        break
