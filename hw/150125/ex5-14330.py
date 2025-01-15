from itertools import product

for pos, val in enumerate(product('0123456789', repeat=5), 1):
    maxx = -1
    minn = 10
    summ = 0
    val = ''.join(val)
    for i in val:
        i = int(i)
        if i > maxx:
            maxx = i
        if i < minn:
            minn = i
    for i in val:
        if int(i) % 2 == 0:
            summ += int(i)
    strr = str((maxx + minn) ** 2) + str(summ)
    if strr == '12116':
        print(pos)
        break
