from itertools import permutations, product


def f(x, y, w, z):
    return (not(x == (w and (not z)))) and (y == (x and (not w)))

for i in product([0, 1], repeat=6):
    table = [(i[0], i[1], 0, i[2]), (i[3], 0, i[4], 0), (0, i[5], 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xwyz'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)
