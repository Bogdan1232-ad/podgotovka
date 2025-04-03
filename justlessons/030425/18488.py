def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(100):
    s = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    s = convert(s, 7)
    if s.count('6') == 49:
        print(x)
        break

# l = []
# for x in range(2031):
#     s = 3 ** 100 - x
#     s = convert(s, 3)
#     if s.count('0') == 1:
#         l.append(x)
# print(max(l))