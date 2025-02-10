with open('17_9786.txt') as file:
    data = [int(i) for i in file]

l = []
max_25 = max(i for i in data if str(i)[-2:] == '25')

for i in range(len(data) - 2):
    a1 = data[i]
    a2 = data[i + 1]
    a3 = data[i + 2]

    u1 = len(str(abs(a1))) == 4
    u2 = len(str(abs(a2))) == 4
    u3 = len(str(abs(a3))) == 4

    if a1 + a2 + a3 <= max_25:
        if u1 + u2 + u3 <= 2:
            l.append(a1 + a2 + a3)

print(len(l), max(l))