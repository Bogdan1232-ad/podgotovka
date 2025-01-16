from itertools import product, permutations


# first way
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (not(((not x) or y) and (not w))) or (not (z and (not (y and w))))
#                 if not(f):
#                     print(y, x, w, z)

def f(x, y, z, w):
    f = (not (((not x) or y) and (not w))) or (not (z and (not (y and w))))


for i in product([0, 1], repeat=7):
    table = [(0, i[0], i[1], 1), (i[2], 1, i[3], i[4]), (1, 0, i[5], i[6])]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)
