def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 2006):
    s = (4 ** 163) * 5 + (12 ** 62) - x
    s = convert(s, 5)
    if s.count('1') < s.count('4'):
        print(x)