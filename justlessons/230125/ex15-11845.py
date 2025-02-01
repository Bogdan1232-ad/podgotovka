def de(x, y):
    return x % y == 0


def f(a):
    for x in range(1, 10000):
        if not ((de(a, x) <= ((x == a) or (x == 1)))):
            return False
    return True


cou = 0
for a in range(1, 11112):
    if f(a):
        cou += 1

print(cou)
