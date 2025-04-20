from itertools import product

alph = sorted('ЛУНАТИК')

l = []

for pos, val in enumerate(product(alph, repeat=6), 1):
    val = ''.join(val)
    gl = val.count('У') + val.count('А') + val.count('И')
    if gl == 1 and val[0] == 'Н':
        l.append(pos)
    if pos == 83635:
        print(val)
print(max(l))