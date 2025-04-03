from itertools import product, repeat

alph = sorted('АРГУМЕНТ')
ans = []
for pos, val in enumerate(product(alph, repeat=4), 1):
    val = ''.join(val)
    if sorted(list(val)) == list(val) and len(set(val)) == len(val):
        ans.append(pos)

print(max(ans))
