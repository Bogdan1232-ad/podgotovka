from itertools import product, permutations

alph = sorted("ШКОЛА")

for pos, val in enumerate(product(alph, repeat=5), 1):
    val = ''.join(val)
    if val == 'ШАЛАШ':
        print(pos)
        break
