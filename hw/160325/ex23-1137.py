def zer(x):
    return x + '0'


def one(x):
    return x + '1'

def plus(x):
    return bin(int(x, 2) + 1)[2:]


def f(x, y):
    if x == str(y):
        return 1
    if int(x) > y:
        return 0
    return f(zer(x), y) + f(one(x), y) + f(plus(x), y)


print(f('100', 11101))
