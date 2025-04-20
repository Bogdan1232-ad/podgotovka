with open('17_2399.txt') as file:
    data = [int(i) for i in file]

sum_35 = sum([i for i in data if i % 35 == 0])
l = []
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    u1 = (a > sum_35) != (b > sum_35)
    u2 = (hex(a)[-2:] == 'ef') != (hex(b)[-2:] == 'ef')
    if u1 and u2:
        l.append(a + b)


# print(len(l), min(l))