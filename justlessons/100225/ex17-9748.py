with open('17_9748.txt') as file:
    data = [int(i) for i in file]

l = []
max_15 = max(i for i in data if str(i)[-2:] == '15')

for i in range(len(data) - 2):
    a1 = data[i]
    a2 = data[i + 1]
    a3 = data[i + 2]
    a11 = len(str(a1)) == 4
    a22 = len(str(a2)) == 4
    a33 = len(str(a3)) == 4
    if a1 + a2 +a3 >= max_15:
        if a11 + a22 + a33 == 1:
            l.append(a1 + a2 + a3)

print(len(l), max(l))