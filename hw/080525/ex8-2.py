from itertools import product

alp = sorted('ЦАПЛЯ')

for pos, val in enumerate(product(alp, repeat=5), 1):
    val = ''.join(val)
    if val.count('А') <= 1 and val.count('Ц') == 2 and 'Л' not in val:
        print(pos)
        break

