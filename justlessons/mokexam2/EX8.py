from itertools import product

alph = '0123456789AB'

cou = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    bol_8 = i.count('9') + i.count('A') + i.count('B')
    if i.count('7') == 1 and bol_8 <= 3 and i[0] != '0':
        cou += 1
print(cou)