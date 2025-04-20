def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

l_4 = set()
for x in range(3, 2025):
    s = 5 ** 2025 + 5 ** 200 - x
    s = convert(s, 5)
    l_4.add(str(s).count('4')) # 199
    if str(s).count('4') == 199:
        print(x)
print(max(l_4))