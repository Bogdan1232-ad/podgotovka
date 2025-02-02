from itertools import product, permutations

def f(x, y, z, w):
    return (w and y) or ((x <= w) == (y <= z))

for i in product([0, 1], repeat=6):
    table = [(i[0], i[1], i[2], 1),\
             (1, i[3], i[4], 1), \
             (1, i[5], 1, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)