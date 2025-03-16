for p in range(16, 37):
    x1 = int('17496', p)
    x2 = int('91F83', p)
    x3 = int('D9543', p)
    if (x1 + x2 + x3) % 12 == 0:
        print((x1 + x2 + x3) // 12 )
