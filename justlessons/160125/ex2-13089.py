from itertools import product, permutations

def f(x, y, w, z, u):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))

for i in product([0, 1], repeat=8):
    table = [(0, i[0], 0, 0, 0), (0, i[1],i[2], 0, 0), (i[3], 0, 0, 0, i[4]), (0, 0, i[5], i[6], i[7])]
    if len(table) == len(set(table)):
        for p in permutations('xywzu'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0, 0]
            if u:
                print(*p)
