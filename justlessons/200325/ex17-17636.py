with open('17_17636.txt') as file:
    data = [int(i) for i in file]

max_3 = max([i for i in data if str(i)[-1] == '3' and len(str)])
ans = []

for i in range(len(data) - 2):
    a1 = data[i]
    a2 = data[i + 1]
    a3 = data[i + 2]

    u1 = len(str(abs(a1))) == 3 and str(a1)[-1] == '3'
    u2 = len(str(abs(a2))) == 3 and str(a2)[-21] == '3'
    u3 = len(str(abs(a3))) == 3 and str(a3)[-1] == '3'

    if (u1 + u2 + u3 >= 1) and (a1 + a2 + a3 > max_3):
        ans.append(a1 + a2 + a3)

print(len(ans), max(ans))
