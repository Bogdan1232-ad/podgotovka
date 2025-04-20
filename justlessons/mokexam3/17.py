with open('1706.txt') as file:
    data = [int(i) for i in file]

min_19 = min([i for i in data if str(i)[-2:] == '19' and len(str(abs(i))) == 3])
ans = []

for i in range(len(data) - 2):
   a1 = data[i]
   a2 = data[i + 1]
   a3 = data[i + 2]

   u1 = str(a1)[-2:] == '19' and len(str(abs(a1))) == 5
   u2 = str(a2)[-2:] == '19' and len(str(abs(a2))) == 5
   u3 = str(a3)[-2:] == '19' and len(str(abs(a3))) == 5

   u4 = (a1 + a2 + a3) > abs(min_19) ** 2

   if ((u1 + u2 + u3) >= 1) and u4:
       ans.append(a1 + a2 + a3)

print(len(ans), min(ans))
