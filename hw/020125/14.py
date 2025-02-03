from string import ascii_uppercase, digits

for x in range(150):
    x1 = 5 * 150 ** 4 + 1 * 150 ** 3 + x * 150 ** 2 + 2 * 150 + 9
    x2 = x * 150 ** 3 + 0 + 2 * 150 + 3
    if (x1 + x2) % 149 == 0:
        print((x1 + x2) // 149)
