from itertools import product


def f(num):
    divs = set()
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)
    return sorted(divs)

def summ(x):
    summ = 0
    for i in x:
        summ += i
    return summ


for i in product('0123456789', repeat=4):
    for z in '0123456789':
        i = ''.join(i)
        z = ''.join(z)
        num = i + '7' + z
        if num[0] != '0' and len(f(int(num))) >= 18 and int(num) >= 400_000 and int(num) <= 500_000:
            print(num, summ(f(int(num))))

