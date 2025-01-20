from itertools import product, permutations

def f(a, b, c, d):
    return (not (b <= c)) and (c <= b) or \
        a and b and c and (not d)

for i in product([0, 1], repeat=9):
    table = [(i[0], 0, 0, 0), (i[1], i[2], i[3], 0), \
             (i[4], i[5], 0, 0), (i[6], 0, i[7], i[8])]
    if len(table) == len(set(table)):
        for p in permutations('abcd'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1 ,1 ,1]
            if u:
                print(*p)
