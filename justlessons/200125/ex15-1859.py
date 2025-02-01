# l = []
# for a in range(-100, 100):
#     flag = True
#     for x in range(1, 100):
#         for y in range(1, 100):
#             if not(((2*x + y) != 70) or (x < y) or (a < x)):
#                 flag = False
#     if flag:
#         l.append(a)
# print(max(l))

def f(A):
    for x in range(0, 10000):
        for y in range(0, 10000):
            f = (2 * x + y != 70)\
                or (x < y) or (A < x)
            if not(f):
                return False
    return True


for A in range(-10000, 100)[::-1]:
    if f(A):
        print(A)
        break

