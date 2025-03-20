with open('17_14952 (1).txt') as file:
    data = [int(i) for i in file]

max_121 = max([i for i in data if str(i)[-3:] == '121'])

l = []
for i in range(len(data) - 2):
    a1, a2, a3 = data[i], data[i + 1], data[i + 2]

    u1 = len(str(abs(a1))) == 4 and a1 % 2 == 0
    u2 = len(str(abs(a2))) == 4 and a2 % 2 == 0
    u3 = len(str(abs(a3))) == 4 and a3 % 2 == 0

    if (u1 + u2 + u3) <= 1 and (a1 +  a2 + a3) <= max_121:
        l.append(a1 + a2 + a3)

print(len(l), max(l))
