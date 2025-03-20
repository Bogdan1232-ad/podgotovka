from string import ascii_uppercase, digits

alph = digits + ascii_uppercase
alph = alph[:25]
for i in alph:
    x1 = int('A4' + i + '7F2', 25)
    x2 = int('N' + i + 'G5' + i + 'H', 25)
    x3 = int("74" + i + 'M26', 25)
    summ = x1 + x2 + x3
    if summ % 24 == 0:
        print(summ // 24)
