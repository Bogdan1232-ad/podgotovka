from itertools import product

for j in range(3):
    for i in product('0123456789', repeat=j):
        i = ''.join(i)
        num = '12' + i + '4'
        for v in '0123456789':
            num1 = num + v + '65'
            num1 = int(num1)
            if num1 % 161 == 0 and num1 < 10 ** 8:
                print(num1, num1 // 161)
