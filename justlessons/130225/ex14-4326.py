from string import digits, ascii_uppercase
from collections import Counter
alph = digits + ascii_uppercase

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num//=sys
    return res[::-1]

s = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
s = convert(s, 15)
print(Counter(s))
print(s)