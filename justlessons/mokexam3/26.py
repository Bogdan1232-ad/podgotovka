with open('2600 (1).txt') as file:
    n = file.readline()
    data = [list(map(int, i.split())) for i in file]

def okr(num):
    if num / 10 != num // 10:
        return num // 10 + 1
    return num // 10


data = sorted(data)
summ = 14

for i in range(13, len(data) - 1):
    a1 = okr(data[i][1])
    a2 = okr(data[i + 1][1])

    if a1 + data[i][0] <= data[i + 1][0]:
        summ += a2 + data[i + 1][0]

print(summ)