def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(1001)[::-1]:
    s = convert(n, 7)
    if n % 2 == 0:
        s = '52' + s + '1'
    else:
        if s[-1] == '0':
            s = s[1:-1] + s[0] + '15'
        else:
            s = s[-1] + s[1:-1] + s[0] + '15'
    if len(s) == 4:
        print(n)
        break
