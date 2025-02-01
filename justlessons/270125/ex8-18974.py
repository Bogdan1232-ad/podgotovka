from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase[:15]
cou_nech = 0
cou_5 = 0
cou = 0
for i in product(alph, repeat=4):
    i = ''.join(i)
    for j in i:
        if j in alph[1::2]:
            cou_nech += 1
        if j in '012345':
            cou_5 += 1
    if cou_nech == 1 and cou_5 <= 2 and i[0] != '0':
        cou += 1
    cou_5 = 0
    cou_nech = 0

print(cou)
