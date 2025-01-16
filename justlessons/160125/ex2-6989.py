from itertools import product,permutations

def f(x, y,z):
    return x <= (y and z)


table = [(0, 1, 0), (1, 1, 0)]
if len(table) == len(set(table)):
    for p in permutations('xyz'):
        u = [f(**dict(zip(p, t))) for t in table] == [0 ,0]
        if u:
            print(*p)