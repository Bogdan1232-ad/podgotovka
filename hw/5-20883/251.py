from fnmatch import fnmatch

def dell(num):
    l = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            l.add(num // i)
            l.add(i)
    return l


for i in range(10 ** 6):
    cnt = 0
    for j in dell(i):
        if fnmatch(str(j),'4*'):
            cnt += 1
    if cnt == 24:
        pass