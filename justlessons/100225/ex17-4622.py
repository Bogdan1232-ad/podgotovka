with open('17_4622.txt') as file:
    data = [int(i) for i in file]

min_19 = min([i for i in data if i % 19 == 0 and i > 0])
l = []

for i in range(1, len(data)):
    a1 = data[i - 1]
    a2 = data[i]

    if (a1 + a2) < min_19:
        l.append(a1 + a2)

print(len(l), max(l))
