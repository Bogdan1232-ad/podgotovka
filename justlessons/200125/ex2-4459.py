from itertools import product, permutations

def f(x, y, w, z):
    return ((not x) <= y) and ((not y) == z) and w

for i in product([0, 1], repeat=8):
    table = [(0, i[0], 0, i[1]), (0, i[2], i[3], i[4]), \
            (i[5], 0, i[6], i[7])]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)