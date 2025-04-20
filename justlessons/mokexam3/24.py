with open('2418.txt') as file:
    data = file.readline()

while '++' in data or '+*' in data or '**' in data or '*+' in data:
    data = data.replace('+*', ' ').replace('*+', ' ').replace('++', ' ').replace('**', ' ')

data = data.split()

l = []
for i in data:
    i = i.removeprefix('*')
    i = i.removeprefix('+')
    i = i.removesuffix('*')
    i = i.removesuffix('+')
    if eval(i) % 2 == 0:
        l.append(i)
    if len(i) == 164 and eval(i) % 2 == 0:
        print(i)

print(len(max(l, key=len)))