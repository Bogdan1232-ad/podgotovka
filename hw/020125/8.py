from itertools import product

alph = '0123456789AB'
cou = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    flag = False
    if val.count('B') == 2:
        if val[0] in alph[::2]:
            for i in range(1, len(val)):
                if i % 2 == 0:
                    if val[i] in alph[::2]:
                        flag = True
                else:
                    if val[i] in alph[1::2]:
                        flag = True
        else:
            for i in range(1, len(val)):
                if i % 2 == 0:
                    if val[i] in alph[1::2]:
                        flag = True
                else:
                    if val[i] in alph[::2]:
                        flag = True
    if flag:
        cou += 1
print(cou)