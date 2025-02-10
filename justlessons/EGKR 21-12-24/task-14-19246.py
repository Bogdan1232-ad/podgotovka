from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:25]:
    x1 = int('11353' + x + '12', 25)
    x2 = int('135' + x + '21', 25)
    if (x1 + x2) % 24 == 0:
        print((x1 + x2) // 24)

