from itertools import product

alp = '012345678'

def triada(num):
    for i in range(len(num) - 2):
        if num[i] == num[i+1] == num[i+2]:
            return False
    return True

cnt = 0
for digits in product(alp, repeat=7):
    num = ''.join(digits)
    if num[0] != '0' and num[-1] not in '347' and triada(num):
        cnt += 1

print(cnt)