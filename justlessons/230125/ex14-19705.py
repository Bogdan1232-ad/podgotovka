def convert(num, sys):
    st = ''
    while num:
        st += str(num % sys)
        num//=sys
    return st[::-1]

for x in range(1, 2006)[::-1]:
    s = 43 ** 56 + 113 ** 841 - x
    s = convert(s, 4)
    chet = s.count('0') + s.count('2')
    nechet = s.count('1') + s.count('3')

    cou_2 = s.count('2')

    if chet%2 == 0 and nechet%2 == 0 and cou_2<=712:
        print(x)
        break