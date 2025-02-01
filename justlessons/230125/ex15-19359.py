from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:12]
for x in alph:
    summ = int('A23' + x + 'AC0', 22) + int('GB' + x + '21670', 22)
    if summ % 21 == 0:
        print(summ//22)