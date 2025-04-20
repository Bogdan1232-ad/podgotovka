from itertools import product, permutations

def f(w, x, y, z):
    return x and ((z <= y) == w)

for i in product([0, 1], repeat=5):
    table = [(1, i[0], 1, i[1]), (0, i[2], 1, 1), (1, 1, 1, i[3]), (1, 1, 1, i[4])]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) for t in table):
                print(*p)

for x in [0, 1]:
    for y in [0, 1]:
        for w in [0, 1]:
            for z in [0, 1]:
                if f(w, x, y, z):
                    print(w, y, x, z)