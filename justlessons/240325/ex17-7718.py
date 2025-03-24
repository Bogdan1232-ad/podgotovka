with open('17 (2)_7718.txt') as file:
    data = [int(i) for i in file]

l = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] != data[j]:
            if (((i + j) % 18 == 0) +( (i * j) % 18 == 0)) == 1:
                l.append(i + j)

print(len(l), max(l))