def f_2(num):
    for i in range(1000):
        if i ** 2 == num:
            return True
    return False

def dell(num):
    l = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 and f_2(i):
            l.add(num // i)
            l.add(i)
        if not dell:
            pass
    return l

for i in range(10 ** 6, 10 ** 20):
    if len(dell(i)) >= 20:
        print(i, sum(dell(i)))