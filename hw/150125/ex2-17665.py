from itertools import product, permutations


# first way
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (z <= (not (y <= x))) or w
#                 if not(f):
#                     print(z, y, x, w, int(f))

def f(x, y, z, w):
    return (z <= (not (y <= x))) or w


for i in product([0, 1], repeat=7):
    table = [(i[0], 1, i[1], i[2]), (i[3], i[4], 0, 0), (i[5], 0, 1, i[6])]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)
