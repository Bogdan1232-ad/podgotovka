def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

l = set()
for x in range(1, 2031):
    s = 2 ** 2025 + 2 ** 2024 - 2 ** 2021 - x
    cou_4 = convert(s, 4)
    l.add(cou_4.count('0'))
    if cou_4.count('0') == 5:
        print(x)

print(max(l))