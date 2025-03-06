l = []
for n in range(1, 13):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    s = int(s, 2)
    l.append(s)
print(max(l))