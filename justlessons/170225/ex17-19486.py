with open("17_19486.txt") as file:
    data = [int(i) for i in file]

lenn = len([i for i in data if str(i)[-1] == '7'])

ans = []

for i in range(len(data) - 1):
    if (data[i] > 0 and data[i + 1] < 0) or \
            (data[i] < 0 and data[i + 1] > 0):
        if data[i] + data[i + 1] < lenn:
            ans.append(data[i] + data[i + 1])
print(len(ans), max(ans))