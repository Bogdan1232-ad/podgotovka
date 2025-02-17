from itertools import product, permutations

def f(x, y, w, z):
    return (not w) and ((y or z) <= (y and (not x)))

for i in product([0, 1], repeat=8):
    table = [(i[0], i[1], i[2], 1), (i[3], i[4], 1, i[5]), (i[6], 1, 1, i[7])]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)