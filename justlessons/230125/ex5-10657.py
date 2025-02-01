def convert(num, sys):
    st = ''
    while num:
        st += str(num % sys)
        num//=sys
    return st[::-1]

l =  set()
for n in range(1, 1000):
    s = convert(n, 3)
    if sum(map(int, s)) % 3 == 0:
        s = '20' + s
    else:
        s = '10' + s

    s = int(s, 3)
    if s < 100:
        l.add(n)

print(max(l))