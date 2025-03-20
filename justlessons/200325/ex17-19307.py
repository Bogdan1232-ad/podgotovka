def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

s = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625** 4 - 2005
s = convert(s, 5)
print(s.count('0'))