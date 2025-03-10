def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]

for x in range(100):
    s = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    if convert(s, 7).count('6') == 49:
        print(x)
        break