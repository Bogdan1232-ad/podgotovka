with open('24_8510.txt') as file:
    data = file.readline()

data = data.replace('NO', '*').replace('ON', '*').replace('OP', '*').replace('PO', '*').replace('NP', '*').replace('PN', '*')

l = set()
for i in range(len(data)):
    for j in range(i, len(data)):
        if '*' not in data[i:j]:
            l.add(len(data[i:j]))
print(max(l))