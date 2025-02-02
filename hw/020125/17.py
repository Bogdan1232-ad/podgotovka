with open("17_8562.txt") as file:
    data = [int(i) for i in file]

min_2 = min([i for i in data if len(str(abs(i))) == 2 and str(i)[-1] == '1'])
print(min_2)
min_2 = min_2 ** 2


l = []
for i in range(1, len(data)):
    if data[i - 1] + data[i] >= 0:
        u1 = abs(data[i - 1]) ** 2 < min_2
        u2 = abs(data[i]) ** 2 < min_2
        if u1 + u2 == 1:
            l.append(u1 + u2)
print(len(l), min(l))