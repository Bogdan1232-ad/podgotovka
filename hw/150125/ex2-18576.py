from itertools import product, permutations


# u don't have to type y or y, it's pointless
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = (not(w<=(x == (y or y)))) and (z <= x)
#                 if f:
#                     print(y, x, w, z)

def f(x, y, w, z):
    return (not (w <= (x == (y or y)))) and (z <= x)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, 1, 1, a2), (0, a3, a4, 0), (a5, 0, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)
