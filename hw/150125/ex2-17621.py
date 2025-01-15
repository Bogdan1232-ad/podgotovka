from itertools import permutations, product


def f(x, y, w, z):
    return (not (x <= z)) or (y == w) or y

for i in product([0, 1], repeat=7):
    table = [(1, 0, i[0], i[1]), (i[2], 1, 0, i[3]), (0, i[4], i[5], i[6])]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)