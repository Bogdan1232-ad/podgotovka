ans = []
for n in range(4, 10000):
    s = '1' + n * '9'

    s = s.replace('19', '9')
    s = s.replace('49', '91')
    s = s.replace('999', '4')
    ans.append(sum(map(int, s)))

print(max(ans))