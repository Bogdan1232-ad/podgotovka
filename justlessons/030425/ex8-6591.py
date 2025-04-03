from itertools import product


def sumchet(num):
    even = 0
    odd = 0
    for i in num:
        if int(num) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    if even < odd:
        return True
    return False


alph = '0123456'
cou = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] != '0' and i.count('6') == 1 and sumchet(i):
        cou += 1
print(cou)