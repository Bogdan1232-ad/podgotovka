from itertools import product 

alp = '01234'
cnt = 0
for i in product(alp, repeat=6):
	i = ''.join(i)
	if i[0] == '3':
		if int(i) % 2 == 0:
			cnt += 1
print(cnt)