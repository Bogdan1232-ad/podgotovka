def convert(num, sys):
    res= ''
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]

l = set()
for n in range(1, 1000):
    s = convert(n, 3)
    if n%3 == 0:
        s = s + s[-2:]
    else:
        s = s + convert(sum(map(int, s)), 3)
    s = int(s, 3)
    if s>220 and s%2==0:
        l.add(s)
print(min(l))