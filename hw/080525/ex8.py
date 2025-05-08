def convert(num, sys):
    res = ''
    while num:
        res += str(num & sys)
        num //= sys
    return res[::-1]

cnt = 0
for i in range(10**7, 10**8):
    i = convert(i, 7)
    if i[0] != '0' and i[0] not in '02468' and i[-1] not in '0124578' \
            and i.count('6') >= 1:
        cnt += 1

print(cnt)
