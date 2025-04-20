def convert(num, sys):
	res = ''
	while num:
		res += str(num % sys)
		num //= sys
	return res[::-1]

for n in range(10000)[::-1]:
	s = convert(n, 3)
	if n % 5 == 0:
		s = s + s[-3:]
	else:
		s += convert((n % 5) * 5, 3)
	if int(s, 3) <= 5496:
		print(n)
		break