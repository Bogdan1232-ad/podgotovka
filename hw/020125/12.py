for n in range(2, 1000):
    s = '>' + 21 * '0' + n * '1' + 11 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    s = s.replace('>', '')
    if sum(map(int, s)) % n == 0:
        print(n)
        break

# либо 1, либо 43
