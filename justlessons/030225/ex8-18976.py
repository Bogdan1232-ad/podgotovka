from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

alph = alph[:20]
cou = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] != "0" and\
            int(i[0], 20) + int(i[-1], 20) == 26:
        for j in alph[::2]:
            i = i.replace(j, '*')
        for j in alph[1::2]:
            i = i.replace(j, '_')
        if '**' not in i and '__' not in i:
            cou += 1
print(cou)