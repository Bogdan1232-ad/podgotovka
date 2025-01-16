from itertools import product, permutations

def f(x, y, z, w):
    return w and ((z or y)) == (z and x)

for i in product([0, 1], repeat=5):
    table = [(1, i[0], 1, 0), (0, i[1], i[2], i[3]), (1, 1, 1, i[4])]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 0]
            if u:
                print(*p)