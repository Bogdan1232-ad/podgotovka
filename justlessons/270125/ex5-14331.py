def convert(num, sys):
    st = ''
    while num:
        st += str(num % sys)
        num//=sys
    return st[::-1]

l = []
for i in range(0, 10000):
    s = convert(i, 3)
    if sum(map(int, s)) % 3 == 0:
        s = s + '212'
    else:
        s = s + convert(sum(map(int, s)) * 2, 3)
    r = int(s, 3)
    if r > 490:
        l.append(r)
print(min(l))