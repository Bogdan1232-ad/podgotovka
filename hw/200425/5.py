for n in range(1000):
    r = bin(n)[2:]
    r = r.replace('1', '*').replace('0', '1').replace('*', '0')
    r = '1' + r
    if r.count('1') % 2: r += '0'
    else: r += '1'
    r = int(r, 2)
    if r > 180:
        print(n)
        break