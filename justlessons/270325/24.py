with open('24_4643.txt') as file:
    data = file.readline()

data = data.replace('A', 'B').replace('1', '2')
data = data.replace('22B', '*')
cou = 0
l = set()
for i in data:
    if i == '*':
        cou += 1
    else:
        cou = 0
    l.add(cou)
print(max(l))
