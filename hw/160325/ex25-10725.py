from itertools import product


def dell(num):
    l = set()
    for i in range(2, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            l.add(i)
            l.add(num // i)
    return l


def summ(x):
    summ = 0
    for i in x:
        summ += i
    return summ


cou = 0
for i in range(3):
    for z in product('0123456789', repeat=i):
        for i1 in range(3):
            for z1 in product('0123456789', repeat=i):
                for v in '0123456789':
                    z = ''.join(z)
                    z1 = ''.join(z1)
                    num = '6' + z + '97' + z1 + '5' + v
                    if len(dell(int(num))) >= 4 and int(num) > 65000:
                        cou += 1
                        print(num, summ(dell(int(num))))
    if cou == 7:
        break
