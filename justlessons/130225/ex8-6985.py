from itertools import product, repeat
from collections import Counter

alph = sorted('МАРКСЛ')
l = []

for pos, val in enumerate(product(alph, repeat=6), 1):
    val = ''.join(val)
    if 'СК' not in val and 'КС' not in val:
        son = Counter(val)
        flagg = False
        cou = 0
        for i in son.items():
            if i[1] == 3:
                flagg = True
            if i[1] == 1:
                cou += 1
        if flagg and cou == 3:
            l.append(pos)

print(max(l))