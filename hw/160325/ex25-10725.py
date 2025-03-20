from itertools import product
from fnmatch import fnmatch

def dell(num):
    l = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and i % 2 == 0:
            l.add(i)
        if num % i == 0 and (num // i) % 2 == 0:
            l.add(num // i)
    return l

cou = 0

for i in range(65000, 10**6):
    if fnmatch(str(i), '6*97*5?'):
        if len(dell(i)) >= 4:
            print(i, sum(dell(i)))
            cou += 1
    if cou == 7:
        break
cou = 0
l = []
# for i in range(2):
#     for z in product('0123456789', repeat=i):
#         for i1 in range(2):
#             for z1 in product('0123456789', repeat=i1):
#                 for v in '0123456789':
#                     z = ''.join(z)
#                     z1 = ''.join(z1)
#                     num = '6' + z + '97' + z1 + '5' + v
#                     if len(dell(int(num))) >= 4 and int(num) > 65000:
#                         cou += 1
#                         l.append([num, summ(dell(int(num)))])

# for i in range(65000, )
# print(sorted(l)[:7])

