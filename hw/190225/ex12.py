for n in range(4, 10000):
    s = '5' + '2' * n
    s = s.replace('52', '11')
    s = s.replace('2222', '5')
    s = s.replace('1122', '25')
    if str(sum(map(int, s)))[-1] == '7':
        print(n, str(sum(map(int, s))), s)
        break