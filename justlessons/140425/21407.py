from itertools import product

cnt = 0
alp = sorted('ДГИАШЭ')
for i in product(alp, repeat=5):
    i = ''.join(i)
    if i[0] not in 'ИАЭ' and i[-1] not in 'ДГШ':
        cnt += 1
print(cnt)