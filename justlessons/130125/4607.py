from itertools import product, permutations, permutations

def f(x, y, z, w):
    return ((x <= z) <= y) or (not w)

for i in product([1, 0], repeat=7):
    table = [(1, 0, i[0], i[1]), (i[2], 1, 0, i[3]), (0, i[4], i[5], i[6])]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)